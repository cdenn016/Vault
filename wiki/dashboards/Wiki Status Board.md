---
type: moc
title: Wiki Status Board
aliases: [Wiki status, Maturity board, Status board]
tags: [moc]
status: stable
created: 2026-06-19
updated: 2026-06-19
---

# Wiki Status Board

> Maturity tracker for the **synthesis layer** (`wiki/` pages), grouped by the `status` frontmatter
> field (`stub` → `draft` → `stable`). A live **Bases** view; promote a page by changing its
> `status:` to `stable` once its synthesis is mature and source-verified. Most pages are still
> `draft` — the core hub concepts (Fisher information, VFE, gauge transformation, …) were promoted
> to `stable` first. Source notes are excluded (this scopes to `wiki/`).

## Stable — canonical, source-verified

```base
filters:
  and:
    - 'file.inFolder("wiki")'
    - 'status == "stable"'
views:
  - type: table
    name: "Stable"
    order:
      - title
    properties: [file.name, title, type]
```

## Draft — written, not yet promoted

```base
filters:
  and:
    - 'file.inFolder("wiki")'
    - 'status == "draft"'
views:
  - type: table
    name: "Draft"
    order:
      - title
    properties: [file.name, title, type]
```

## Stub — placeholder, needs expansion

```base
filters:
  and:
    - 'file.inFolder("wiki")'
    - 'status == "stub"'
views:
  - type: table
    name: "Stub"
    order:
      - title
    properties: [file.name, title, type]
```

## See also
- [[Sources Dashboard]] · [[Disciplines MOC]] · [[index|Index]] · [[LLM-Wiki Schema]]
