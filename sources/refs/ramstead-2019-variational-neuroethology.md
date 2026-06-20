---
type: reference
title: "A tale of two densities: active inference is enactive inference (variational neuroethology and Markov blankets)"
aliases: ["Ramstead 2019", "Ramstead et al. 2019", "Variational neuroethology"]
authors: ["Maxwell J. D. Ramstead", "Paul B. Badcock", "Karl J. Friston"]
year: 2019
tags: [cluster/vfe, project/transformer, project/multi-agent, field/neuroscience, field/biology, field/philosophy]
created: 2026-06-18
updated: 2026-06-18
---

# A tale of two densities: active inference, variational neuroethology, and Markov blankets

> [!info] Citation
> Ramstead, M. J. D., Badcock, P. B., & Friston, K. J. (2019). *Variational neuroethology and the free-energy principle*, in the lineage of "A tale of two densities" / "Answering Schrödinger's question: A free-energy formulation." This note covers the variational-neuroethology programme that interprets the free-energy principle (FEP) through the lens of Markov blankets, generative models, and recognition densities. See BibTeX below.

> [!note] Editorial: The author-supplied slug pairs *variational neuroethology* (Ramstead, Badcock & Friston, *Physics of Life Reviews* 2018) with the *two densities* framing (Ramstead, Kirchhoff & Friston, *Adaptive Behavior* 2019). Both belong to the same Ramstead–Friston FEP-interpretation programme. The frontmatter retains the project-assigned authors (Ramstead, Badcock, Friston) and year (2019); the BibTeX below records the closest matching primary source. Confirm the exact entry against the manuscript's reference list before publication.

## TL;DR

This work clarifies how to read the central constructs of the free-energy principle and active inference: the *generative model* (a creature's implicit model of its niche) and the *recognition density* (its approximate posterior over hidden causes). It frames the FEP around a system's *Markov blanket* — the statistical boundary separating internal states from external states — and shows that minimizing variational free energy is equivalent to a self-evidencing, enactive coupling between an organism and its environment across nested spatial and temporal scales.

## What it establishes

- **Two densities, one boundary.** The FEP rests on a distinction between the *generative density* (joint distribution over sensory and hidden states encoded by the agent) and the *recognition density* (the agent's approximate posterior). The gap between them is scored by [[Variational free energy]], an upper bound on surprisal that the agent minimizes — the same bound expressed elsewhere as the negative [[Evidence lower bound (ELBO)]].
- **Markov blankets as the unit of analysis.** A Markov blanket partitions a system into internal, blanket (sensory + active), and external states. Conditional independence across the blanket is what licenses treating internal states as *inferring* external causes, grounding the "agent" as a statistical individual.
- **Variational neuroethology.** A meta-theoretical ontology that nests the FEP inside Tinbergen's four questions (mechanism, ontogeny, phylogeny, adaptive value), explaining adaptive behaviour across scales as multiscale free-energy minimization.
- **Enactive reading.** Active inference is interpreted as *enactive* rather than narrowly representationalist: the recognition density need not be a literal internal model but a statistical pattern realized in organism–niche dynamics.

## Why the project cites it

The project's gauge-theoretic, multi-agent variational-free-energy program inherits its core objective and its boundary-based notion of agency from this lineage.

- **Foundational objective.** The variational free energy minimized here is the scalar the project lifts into a geometric and gauge-covariant setting; see [[Variational free energy]] and the [[Free-energy principle active inference]] method page.
- **From single agent to many.** The Markov-blanket account of a statistical individual is the conceptual seed for [[Multi-agent variational free energy]] and for [[Meta-agents and hierarchical emergence]] — nested blankets within blankets motivate the project's [[Ouroboros multi-scale dynamics]] and [[Renormalization-group flow of beliefs]].
- **Beliefs as bundle data.** Treating each agent's recognition density as a local posterior attached over a base of contexts connects to [[Agents as fibre-bundle sections]], where a [[Gauge transformation]] reparameterizes the belief frame without changing physical content.
- **Geometry of inference.** The recognition density lives on a statistical manifold whose natural metric is the [[Fisher information metric]]; the project's use of the [[Natural gradient]] and [[Mass as Fisher information]] gives dynamical teeth to free-energy descent that this paper specifies only variationally.
- **Participatory framing.** The self-evidencing, observer-relative reading of inference resonates with [[Participatory realism (it from bit)]], a theme the project develops in [[participatory-it-from-bit]].

Related sources in the same cluster: [[friston-2017-active-inference-process]], [[parr-2022-active-inference]], and the precision/predictive-coding machinery in [[Precision weighting]] and [[Prediction error]].

```bibtex
@article{ramstead2019twodensities,
  title   = {A tale of two densities: active inference is enactive inference},
  author  = {Ramstead, Maxwell J. D. and Kirchhoff, Michael D. and Friston, Karl J.},
  journal = {Adaptive Behavior},
  volume  = {28},
  number  = {4},
  pages   = {225--239},
  year    = {2019},
  doi     = {10.1177/1059712319862774}
}

@article{ramstead2018neuroethology,
  title   = {Answering Schr{\"o}dinger's question: A free-energy formulation},
  author  = {Ramstead, Maxwell J. D. and Badcock, Paul B. and Friston, Karl J.},
  journal = {Physics of Life Reviews},
  volume  = {24},
  pages   = {1--16},
  year    = {2018},
  doi     = {10.1016/j.plrev.2017.09.001}
}
```
