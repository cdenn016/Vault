---
type: "paper"
title: "Conscious agent networks: Formal analysis and application to cognition"
aliases: ["Conscious agent networks: Formal analysis and application to cognition (Fields 2018)"]
authors: ["Chris Fields", "Donald D. Hoffman", "Chetan Prakash", "Manish Singh"]
year: 2018
url: "https://chrisfieldsresearch.com/CA-circuits-CSR-rev2.pdf"
tags: ["cluster/participatory", "cluster/participatory/philosophy-of-mind", "project/multi-agent", "field/cs-ml", "field/psychology", "field/philosophy"]
created: "2026-11-01"
updated: "2026-11-01"
doi: "10.1016/j.cogsys.2017.10.003"
---

# Conscious agent networks: Formal analysis and application to cognition

> [!info] Citation
> Fields, C., Hoffman, D. D., Prakash, C. and Singh, M. (2018) Conscious agent networks: Formal analysis and application to cognition. Cognitive Systems Research 47: 186-213 (doi: 10.1016/j.cogsys.2017.10.003).

Local PDF: [PDF](../pdfs/fields-2018-conscious-agent-networks-formal-analysis-and-application-to-cognition.pdf)

## Summary

The authors model a conscious agent using measurable experience, action, and world spaces linked by perception, decision, and action Markov kernels, together with an update counter. Target-state dependence extends the earlier forgetful-kernel definition. Finite examples and explicit circuit constructions support memory, categorization, attention, and case-based planning. Copying and counting operations build memories of percept-action and action-percept associations; these data structures are specified parts of the architecture. The working analysis assumes homogeneous kernels, so learning changes state occupancy rather than the kernels themselves.

The paper distinguishes an intrinsic perspective, restricted to current experience and represented memory, from an extrinsic network description. It discusses composing networks into agents, but its memory example changes kernels to create new functionality; merely taking Cartesian products changes no behavior. The conclusion leaves a full theory of agent combinations, relative component clocks, developmental formation, and practical testing open. Conscious realism is an interpretive assumption, separate from the stochastic constructions.

## Relevance to this research

This is a concrete precedent for normalized-kernel agents and explicit memory in [[Multi-agent variational free energy]]. It also exposes a shared obligation: specify the retained state and the update mechanism when forming a parent. Its supplied circuit composition does not establish endogenous hierarchical formation, and the paper's FEP interpretation is not an identity between the research program's distinct global, per-agent, and reciprocal objectives.

## Reading and version

PDF pp. 1-2, 6-7, 12-13, 20-21, 29-30, and 45-46: definition, kernel assumptions, composition, memory, and conclusion. Author-linked manuscript dated August 29, 2017; published in Cognitive Systems Research 47 (2018), 186-213.

## BibTeX

```bibtex
@article{fields-2018-conscious-agent-networks-formal-analysis-and-application-to-cognition,
  author = {Fields, Chris and Hoffman, Donald D. and Prakash, Chetan and Singh, Manish},
  title = {Conscious agent networks: Formal analysis and application to cognition},
  year = {2018},
  journal = {Cognitive Systems Research},
  volume = {47},
  pages = {186--213},
  doi = {10.1016/j.cogsys.2017.10.003},
  url = {https://chrisfieldsresearch.com/CA-circuits-CSR-rev2.pdf}
}
```
