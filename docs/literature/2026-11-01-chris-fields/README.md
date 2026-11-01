# Chris Fields literature ingestion, November 1, 2026

The user requested a search of Chris Fields's publications and the download and ingestion of papers relevant to the gauge/VFE program, especially physics understood through communication. The collection is organized in [Chris Fields and physics as communication](../../../wiki/themes/Chris%20Fields%20and%20physics%20as%20communication.md).

The selection contains 109 distinct works. There are 106 local PDFs covering 105 selected works and one related early formulation, 103 new notes based on targeted full-text readings, two preserved existing paper notes with newly associated PDFs, and four new bibliographic records whose full text was unavailable in this search. Thus 107 new source notes were added. Page-specific reading records distinguish the retrieved version from its journal citation; they do not certify every proof in every paper.

## Search scope

The primary discovery sources were the [author's publication website](https://chrisfieldsresearch.com/), his historical CV, the [registered arXiv author feed](https://arxiv.org/a/fields_c_1.atom), the broader [arXiv author-name query](https://export.arxiv.org/api/query?search_query=au%3A%22Fields_Chris%22&start=0&max_results=100), publisher records, Crossref metadata, and NASA NTRS. The author-name query returned 44 records and the registered feed 34; these are different searches.

The current-site catalog contained 126 publication entries, from which 96 papers and one book were selected. Twenty-nine entries were excluded by topic. Eight talks were separately cataloged and were not treated as papers. The archive search added nine distinct downloaded papers and three access-gap records. Two other arXiv discoveries were treated as predecessor or alternate versions of selected works.

Relevance was interpreted broadly to include quantum information and reference frames, system identification and measurement, semantic information flow, active inference and biological organization, memory and temporal structure, perception, and the philosophical interpretation of agents. Nuclear spectroscopy, detailed genomics, art, bibliometrics, and general AI history without a direct connection were excluded. Title and topic screening guided retrieval; selected papers then received targeted readings of the relevant setup, construction, results, and discussion. This is a bounded search across the identified catalogs, not a claim that no additional relevant publication exists.

## Artifacts

| File | Contents |
|---|---|
| [author-catalog.json](author-catalog.json) | Current-site publication entries and links. |
| [selection.json](selection.json) | All 126 entries, selection decisions, topic lanes, and catalog versus corrected metadata. |
| [archive-screening.md](archive-screening.md) | Historical and arXiv coverage, access searches, and primary bibliographic sources. |
| [archive-candidates.json](archive-candidates.json) | Fourteen archive candidates, including version relationships and gaps. |
| [downloads.json](downloads.json) | The 96 current-site paper retrievals, resolved URLs, SHA-256 digests, sizes, and page counts. |
| [archive-downloads.json](archive-downloads.json) | The nine additional PDF retrievals and version-specific provenance. |
| [related-version-downloads.json](related-version-downloads.json) | The additional early decompositional-equivalence PDF and its association. |
| [access-gaps.json](access-gaps.json) | Four bibliographic records awaiting full text. |
| [coverage.json](coverage.json) | Consolidated selection, source-note, PDF, reading, and version mapping. |
| [validation.json](validation.json) | Final file/link, metadata, PDF-provenance, and preservation checks. |

The reading records are [physics-reading.json](physics-reading.json), [archive-physics-reading.json](archive-physics-reading.json), [active-reading.json](active-reading.json), [foundations-current-reading.json](foundations-current-reading.json), and [foundations-archive-reading.json](foundations-archive-reading.json). Extracted text and temporary reading aids are local working material. Every selected work is reachable through the wiki map, and each new full-text note links its PDF under sources/pdfs/.

## Versions and corrections

The metadata distinguishes the source that was read from the publication to which it belongs. Hartl and colleagues' 2026 remapping article has DOI 10.1016/j.plrev.2026.06.009; the website's .011 DOI belongs to Fields's separate commentary. The 2026 complementarity reply has DOI 10.1016/j.plrev.2026.02.002, rather than the parent paper's DOI. Kofman and colleagues' published PDF cites pages 11–45, while the author catalog gives 11–47. Other version and date differences are recorded in the individual notes and reading manifests.

The 2022 neural-network paper's author-linked PDF is the 2021 version of the earlier preprint titled Deep Neural Networks as the Semi-classical Limit of Quantum Neural Networks. It is retained under one canonical work, without claiming that the retrieved preprint is identical to the final article. The 2010 decompositional-equivalence preprint was also downloaded and read at pages 1 and 10. It is associated with the later selected work as a related early formulation, without claiming text identity or membership in the same arXiv version chain, and is not counted as another canonical paper. Its generated cover date is 2018, while its arXiv v3 date is April 21, 2010.

The newly retrieved amplituhedra preprint has Chris Fields as first author. Its first submission was in 2025; the read version is arXiv:2509.19772v3 from July 2026. The observer-ready-state preprint was first submitted in 2009, while the retrieved v3 is from 2011. The ER=EPR article has a 2025 journal year and a November 2024 online release.

Three initial PDF routes needed alternatives: the context/QRF paper was obtained from arXiv:2304.10010, the entanglement-swap paper from arXiv:1902.00788, and the object-individuation paper from its official Frontiers page. All 105 selected-work full-text retrievals succeeded using the recorded final routes.

## Access gaps

| Work | Access result |
|---|---|
| Distributed Information and Computation in Generic Quantum Systems | Springer overview and contents available; full book requires subscription or purchase. First eBook release October 17, 2025; copyright 2026. |
| Observables, measurements, and virtual machines (1995) | Bibliographic metadata confirmed; no open full copy confirmed. |
| Measurement and Computational Description (1996) | Oxford chapter abstract and metadata identified; full text access-gated. |
| Why do we talk to ourselves? (2002) | Bibliographic metadata confirmed; no open full copy confirmed. |

No full-text conclusions are attributed to those four unread works. The Springer record is [here](https://link.springer.com/book/10.1007/978-3-031-97263-8); primary records and search details for the older items are in the archive report.

## Synthesis and limits

The wiki map emphasizes the operational ingredients that recur in these papers: interfaces, source recognition, reference alignment, memory, communication likelihoods, and persistence criteria. It distinguishes those connections from an equivalence between classical gauge-VFE models and quantum information theory. Geometry papers retain their supplied quantum, topological, and spacetime structure; consciousness claims retain their interpretive status.

Specific limitations encountered in the readings are retained in the new source notes. They concern, among other things, the weighted-projector unitarity argument in Decompositional equivalence, the commutation/separability step in Consistent quantum mechanics admits no mereotopology, and the next-step/eventual-halting distinction in the Frame and Halting Problems paper. The collection also records that the living-systems experiment did not demonstrate entanglement. These are scoped reading findings, not a new audit of the entire author corpus.

Two existing immutable sources, friston-2024-federated-inference and prakash-2020-conscious-agents, were preserved. The new synthesis qualifies the older federated note's unsupported exact identification with transported peer-KL coupling. The concept updates also distinguish a statistical blanket, a physical interface, and a global variational objective.

No manuscript edits or new records of the user's experiments were part of this ingestion. The original working files are covered by the preservation comparison in validation.json.
