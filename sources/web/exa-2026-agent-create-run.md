---
type: web
title: "Exa Agent API: create a run, retrieved September 26, 2026"
aliases: ["Exa Agent effort ultra API documentation 2026"]
authors: ["Exa"]
year: 2026
url: "https://exa.ai/docs/reference/agent-api/create-a-run"
tags: [cluster/methodology, project/transformer, project/multi-agent, field/cs-ml]
created: 2026-09-26
---

# Exa Agent API: create a run

## Source and archive

Exa, *Create a run*, official API reference, retrieved September 26, 2026. [Current page](https://exa.ai/docs/reference/agent-api/create-a-run). [Archived HTML](exa-2026-agent-create-run-2026-09-26.html). The reference is versioned here by retrieval date because the online schema can change.

## Reviewed API contract

The endpoint is `POST https://api.exa.ai/agent/runs`. Its `effort` field accepts `ultra`, described as the highest effort tier. The `budget.maxCostDollars` field applies to both `auto` and `ultra`; the documented range is $1–$100 and the omitted default for `ultra` is $20. Thus explicit `effort: "ultra"` can coexist with an explicit budget. This documents a tool setting, not a scientific validation procedure.

## Relevance to this research

Supports reproducible configuration of external literature research under [[Rigorous theory search]]. A completed agent report remains secondary research assistance; source inspection and mathematical reconstruction carry any scientific conclusion. No API credential or private run payload is stored in this note.

## Citation

```bibtex
@misc{ExaAgentCreateRun2026,
  author = {{Exa}}, title = {Create a run: Agent API reference},
  year = {2026}, url = {https://exa.ai/docs/reference/agent-api/create-a-run},
  note = {Retrieved 2026-09-26; official documentation archived locally}
}
```
