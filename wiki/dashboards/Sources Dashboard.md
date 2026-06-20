---
type: moc
title: Sources Dashboard
aliases: [Sources, Source dashboard, Corpus dashboard]
tags: [moc]
status: stable
created: 2026-06-19
updated: 2026-06-19
---

# Sources Dashboard

> A live **Bases** dashboard over the source corpus (every `sources/` note carrying a `field/*`
> tag — i.e. all papers + references). Sort any column by clicking its header, or add a filter in
> the Bases toolbar to slice live by `field/*`, `cluster/*`, `project/*`, year, or author. For a
> discipline-only view use the field MOCs in [[Disciplines MOC]]; for maturity use [[Wiki Status Board]].

## All sources

```base
filters:
  and:
    - 'file.hasTag("field")'
views:
  - type: table
    name: "All sources (A–Z)"
    order:
      - title
    properties:
      - file.name
      - title
      - year
      - tags
  - type: table
    name: "By year"
    order:
      - year
    properties:
      - year
      - title
      - file.name
```

## By project

```base
filters:
  and:
    - 'file.hasTag("field")'
views:
  - type: table
    name: "VFE Transformer"
    filters:
      and:
        - 'file.hasTag("project/transformer")'
    order:
      - title
    properties: [file.name, title, year]
  - type: table
    name: "Multi-agent (MAgent)"
    filters:
      and:
        - 'file.hasTag("project/multi-agent")'
    order:
      - title
    properties: [file.name, title, year]
  - type: table
    name: "SocialPhysics"
    filters:
      and:
        - 'file.hasTag("project/social-physics")'
    order:
      - title
    properties: [file.name, title, year]
```

## See also
- [[Disciplines MOC]] — per-discipline `field/*` MOCs
- [[Wiki Status Board]] — synthesis-page maturity
- [[index|Index]] · [[LLM-Wiki Schema]]
