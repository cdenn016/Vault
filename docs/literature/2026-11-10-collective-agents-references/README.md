# Collective agents references: collection of November 10, 2026

This collection covers the 256 references that the manuscript on communication, coherence and collective agents cites and that the vault did not hold before November 10, 2026. Works by the manuscript's author and references that already had a source note were left out. Each reference has a note under `sources/refs/`, and [[Collective agents literature map]] groups the notes by the question they answer.

## Acquisition

[download_references.py](download_references.py) reads [references.json](references.json), looks for an open copy at arXiv and at the open-access locations that OpenAlex lists for the DOI, and keeps a file only if it is a readable PDF whose first pages carry the first author's surname and a distinctive title word. Nothing behind a sign-in was requested. 109 references have a validated local PDF under `sources/pdfs/`; the other 147 have no open copy that passed validation. [downloads.md](downloads.md) lists both groups, and [provenance.json](provenance.json) records the addresses tried, page counts and file hashes without abstracts or extracted text. The PDFs, the text extracts in `reading/` and the full `download_manifest.json` stay local under the vault's publication policy.

The identity check is mechanical. It does not establish that a file is the version of record, and for the following references the note-writing pass found that the local file is a different version or a different document:

- [[aguilera-2023-free-energy-principle]]: a preprint of the reply, with a later date in its header than the 2023 record.
- [[alos-ferrer-2010-logit-response-dynamics]]: the June 2008 working-paper version.
- [[barnett-2023-dynamical-independence-discovering]]: arXiv version 2, not the journal version.
- [[bourrat-2022-tradeoff-breaking-model]]: the bioRxiv preprint.
- [[catal-2025-belief-sharing-blessing]]: arXiv version 1.
- [[cavagna-2010-scale-free-correlations]]: the arXiv preprint, whose title differs slightly.
- [[chalk-2018-unified-efficient-predictive]]: the 2017 bioRxiv preprint.
- [[champion-2026-reframing-expected-free]]: arXiv version 1.
- [[daft-1984-model-organizations-interpretation]]: a Portuguese-language reprint of 2005 that carries the English abstract.
- [[enke-2019-correlation-neglect-belief]]: the 2013 discussion-paper version.
- [[mackowiak-2009-optimal-sticky-prices]]: the central-bank working-paper version.
- [[makur-2020-broadcasting-random-directed]]: an arXiv version with a different title and abstract.
- [[morris-2002-social-value-public]]: the web appendix of the article, not the article.
- [[raz-2009-estimating-lieb-robinson]]: the arXiv preprint, which carries an earlier title.
- [[shalizi-2025-what-macrostate-subjective]]: the 2003 arXiv preprint as revised in 2024.

One arXiv preprint failed the title check because the journal article was retitled; it was accepted by an explicit override in the script. The copy of one 1960 article written in Russian failed the check on its English title and was not kept.

## Reading basis of the notes

Sixteen agents wrote the notes, each restricted to the text extract of the first pages of the local PDF, the abstract in the OpenAlex record, the reading record kept with the manuscript bibliography, and the bibliographic record. They were told to add nothing from memory. By the basis that each note states, 104 notes draw on a local PDF, 69 on an abstract without a local PDF, 43 on the manuscript reading record alone, and 40 on the bibliographic record alone. No note is a page-by-page reading. A script then checked every note for the prescribed frontmatter, tags from the closed vocabulary, the unchanged BibTeX entry, resolving links and the local-copy line; it restored the frontmatter of three notes, and one note received a missing summary section by hand. The notes were not reviewed against the papers by a second reader.

A few OpenAlex records carried text that was not an abstract (a table of contents, scraped page text, or the abstract of another work); the agents reported these and did not use them.
