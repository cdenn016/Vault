---
type: reference
title: "Mistral 7B"
aliases:
  - "Jiang et al. 2023"
  - "Mistral 7B"
authors:
  - Albert Q. Jiang
  - Alexandre Sablayrolles
  - Arthur Mensch
  - Chris Bamford
  - Devendra Singh Chaplot
  - Diego de las Casas
  - Florian Bressand
  - Gianna Lengyel
  - Guillaume Lample
  - Lucile Saulnier
  - Lélio Renard Lavaud
  - Marie-Anne Lachaux
  - Pierre Stock
  - Teven Le Scao
  - Thibaut Lavril
  - Thomas Wang
  - Timothée Lacroix
  - William El Sayed
year: 2023
arxiv: "2310.06825"
url: https://arxiv.org/abs/2310.06825
tags:
  - cluster/attention
  - project/transformer
  - project/multi-agent
  - field/cs-ml
created: 2026-06-19
updated: 2026-06-19
---

# Mistral 7B

> [!info] Citation
> Albert Q. Jiang, Alexandre Sablayrolles, Arthur Mensch, et al. (2023). "Mistral 7B." arXiv:2310.06825. <https://arxiv.org/abs/2310.06825>

## TL;DR

Mistral 7B is a 7-billion-parameter open-weight decoder-only transformer that outperforms larger models of its day, using grouped-query attention and sliding-window attention for efficient inference over long contexts.

## Relevance to this research

Cited by PIFB ([[participatory-it-from-bit]]) as contemporary architecture furniture — a strong, efficient open baseline in the conventional transformer lineage ([[vaswani-2017-attention]]) against which the project's no-neural-network VFE alternative is positioned. Its sliding-window attention is another instance of the local-coupling prior the project treats as a special case under [[Attention mechanisms — theory and positional structure]].

```bibtex
@article{jiang2023mistral,
  title         = {Mistral 7B},
  author        = {Jiang, Albert Q. and Sablayrolles, Alexandre and Mensch, Arthur and
                   Bamford, Chris and Chaplot, Devendra Singh and de las Casas, Diego and
                   Bressand, Florian and Lengyel, Gianna and Lample, Guillaume and
                   Saulnier, Lucile and Lavaud, L{\'e}lio Renard and
                   Lachaux, Marie-Anne and Stock, Pierre and Le Scao, Teven and
                   Lavril, Thibaut and Wang, Thomas and Lacroix, Timoth{\'e}e and
                   El Sayed, William},
  journal       = {arXiv preprint arXiv:2310.06825},
  year          = {2023},
  eprint        = {2310.06825},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL},
  url           = {https://arxiv.org/abs/2310.06825}
}
```
