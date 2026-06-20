---
type: web
title: "Karpathy — The LLM Wiki Pattern"
aliases:
  - Karpathy — The LLM Wiki Pattern
  - LLM Wiki Pattern
  - Karpathy LLM Wiki
tags:
  - cluster/methodology
author: Andrej Karpathy
year: 2025
url: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
created: 2026-06-18
updated: 2026-06-19
---

# Karpathy — The LLM Wiki Pattern

> [!info] Source
> Andrej Karpathy, "LLM Wiki" gist — <https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f>. The methodological seed for *this* vault.

## Core idea

The pattern makes an LLM's knowledge **compound across sessions** instead of being re-derived every time. Rather than re-reading raw source material at each query (classic retrieval-augmented generation), the LLM incrementally maintains a persistent web of interlinked markdown pages — a personal wiki — and does the bookkeeping itself: summarizing new sources, cross-referencing them against what is already written, reconciling contradictions, and keeping the index current. Humans stay in the loop by curating which sources enter and asking the questions; the LLM owns the synthesis layer.

The architecture is **two layers over an immutable base**:

- **Raw sources** — append-only, never edited; the ground truth (papers, references, run logs, manuscripts).
- **The wiki** — LLM-owned synthesis pages (concepts, methods, themes, projects), freely rewritten as understanding improves.
- A **schema / operating manual** the human and LLM agree on, plus navigation files (an index/catalog and an append-only operations log).

Three operations keep it healthy: **Ingest** (add a source, propagate it into the synthesis pages, log it), **Query** (answer from the wiki first, then bank any non-trivial synthesis back as a page), and **Lint** (periodic health check for contradictions, stale claims, orphans, broken links, duplication, and index drift).

## Relevance to this research

This vault **is** an instance of the pattern, applied to the gauge-theoretic variational-free-energy research program. The conventions encoded in [[LLM-Wiki Schema]] — the immutable `sources/` layer, the LLM-owned `wiki/` synthesis layer, the `[[wikilink]]` graph, the `cluster/*` and `project/*` tag taxonomy, and the Ingest / Query / Lint workflows recorded in the [[log|Operations Log]] — are this pattern made concrete. Both project hubs, [[VFE Transformer Program]] and [[Gauge-Theoretic Multi-Agent VFE Model]], are synthesis pages in the sense Karpathy describes.
