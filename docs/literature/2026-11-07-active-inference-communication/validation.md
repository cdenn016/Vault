# Ingestion validation, November 7, 2026

The collection contains 20 distinct source-note entries paired with 20 local PDFs: 13 new files and seven reused files. All downloads have PDF signatures and open in both pypdf and PyMuPDF, with agreeing page counts. Title and author tokens were checked against the first two pages. The first-page sheets were visually inspected. Gwon's PDF emits nonfatal pypdf object-offset warnings; the original file remains readable and the warnings are retained in the manifest.

Seven new source notes passed required-frontmatter, canonical-wikilink, unique-identity, and local-PDF-link checks. All 20 sources are cited by the synthesis, and the five edited concepts link to it. New source notes are listed in the main index and their discipline maps.

The existing read-only vault lint returned:

```text
files: 1444
BROKEN wikilinks: 0
GRAPH grey nodes: 0
EMPTY files: 0
CASE collisions: 1
    readme ['inbox/README.md', 'README.md']
IDENTITY collisions: 1
    'readme' ['README.md', 'inbox/README.md']
```

The README collision predates this ingestion and was left unchanged. The scoped whitespace check passed. These checks concern the ingestion artifacts and navigation; they are not a verification of every theoretical claim in the papers. The source notes state the sections read and preserve document-version caveats.

Publication preparation retained PDF files, extracted passages, preview images, and the full metadata manifest locally. The compact `provenance.json` publishes acquisition and version records without source abstracts.
