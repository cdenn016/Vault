# PIFB2 remediation, round 2: bibliography changes to `manuscripts/references.bib` (2026-09-24)

Editor: bibliography agent (Claude Opus 5.5). Scope: the eleven keys that the remediated chunks cite but that were missing from the bib, plus the bibliography notes in `digests/GENERAL-integration-notes.md`. No existing entry was deleted, reordered, reformatted or renamed. The new entries are appended in one block after the comment line `% PIFB2 remediation round 2 (2026-09-24) ...`. The file went from 539 to 550 entries. The pre-edit file, including its uncommitted WIP, is a byte-identical prefix of the new file. Line endings remain CRLF and the encoding remains UTF-8.

## Keys added (11)

Each entry was checked against a primary bibliographic record. For DOI entries, the DOI was resolved on Crossref and the title, authors, venue, volume, issue, pages or article number, and year were matched to the metadata in the chunk logs. The two entries without DOIs were checked against zbMATH.

| Key | Work | Verification |
|---|---|---|
| `Amari2009alpha` | S. Amari, "α-Divergence Is Unique, Belonging to Both f-Divergence and Bregman Divergence Classes," IEEE Trans. Inf. Theory 55(11), 4925–4931 (2009) | Crossref, doi 10.1109/TIT.2009.2030485 |
| `Aumann1976` | R. J. Aumann, "Agreeing to Disagree," Ann. Statist. 4(6), 1236–1239 (1976) | Crossref, doi 10.1214/aos/1176343654. Crossref gives no pages, so the pages come from zbMATH 0379.62003 |
| `BarceloLiberatiVisser2011` | C. Barceló, S. Liberati, M. Visser, "Analogue Gravity," Living Rev. Relativ. 14(1), 3 (2011) | Crossref, doi 10.12942/lrr-2011-3 (article number 3) |
| `Caticha2011entropic` | A. Caticha, "Entropic dynamics, time and quantum theory," J. Phys. A: Math. Theor. 44(22), 225303 (2011) | Crossref, doi 10.1088/1751-8113/44/22/225303 |
| `GroveKarcher1973` | K. Grove, H. Karcher, "How to conjugate C¹-close group actions," Math. Z. 132(1), 11–20 (1973) | Crossref, doi 10.1007/BF01214029 |
| `Ito2018` | S. Ito, "Stochastic Thermodynamic Interpretation of Information Geometry," Phys. Rev. Lett. 121(3), 030605 (2018) | Crossref, doi 10.1103/PhysRevLett.121.030605 |
| `Jaynes1957` | E. T. Jaynes, "Information Theory and Statistical Mechanics," Phys. Rev. 106(4), 620–630 (1957) | Crossref, doi 10.1103/PhysRev.106.620 |
| `Lojasiewicz1963` | S. Łojasiewicz, "Une propriété topologique des sous-ensembles analytiques réels," in *Les Équations aux Dérivées Partielles* (Paris, 1962), Colloques Internationaux du CNRS 117, pp. 87–89 (1963) | zbMATH 0234.57007 (no DOI exists). The editor (B. Malgrange) and publisher come from the C07 log and are not in the zbMATH record |
| `PennecArsigny2013` | X. Pennec, V. Arsigny, "Exponential Barycenters of the Canonical Cartan Connection and Invariant Means on Lie Groups," in F. Nielsen, R. Bhatia (eds.), *Matrix Information Geometry*, Springer, pp. 123–166 (2013) | Crossref, chapter doi 10.1007/978-3-642-30232-9_7 (confirms the DOI that C10 left open). The editors and the 2013 print year come from the book record, doi 10.1007/978-3-642-30232-9. The chapter was published online in 2012 |
| `Tikhonov1952` | A. N. Tikhonov, "Systems of differential equations containing small parameters in the derivatives," Mat. Sb. (N.S.) 31(73)(3), 575–586 (1952), in Russian | zbMATH 0048.07101 (no DOI). zbMATH gives the title in German translation; the English title is the one used in the Theory bib |
| `Vandergraft1968` | J. S. Vandergraft, "Spectral Properties of Matrices which have Invariant Cones," SIAM J. Appl. Math. 16(6), 1208–1222 (1968) | Crossref, doi 10.1137/0116101 |

## Mappings to existing keys

There are none. None of the eleven works was already in the bib. The check searched for each DOI and for title and author substrings: "Agreeing to Disagree", "Analogue Gravity", "Entropic dynamics", Barceló, Grove, Ito, Jaynes, Łojasiewicz, Pennec, Tikhonov, Vandergraft, Aumann, and "invariant cones". The following near matches are different works and should not be substituted:

- `jaynes2003probability` is Jaynes's 2003 book, not the 1957 Phys. Rev. paper.
- `Caticha2015` (the 2012 USP Press monograph), `Caticha2019`, `Caticha2019spacetime` and `JohnsonCaticha2011` are different Caticha works from the 2011 J. Phys. A paper.
- `Karcher1977` and the duplicate `karcher1977riemannian` are Karcher's 1977 estimates paper, which C06 cites separately from the 1973 construction.
- `Pennec2006`, `Pennec2009` and `PennecFillardAyache2006` are other Pennec papers.

## Bibliography notes from GENERAL-integration-notes.md

- **C01: WilsonConfinement1974 DOI.** Round 1 already applied this. The entry has `doi = {10.1103/physrevd.10.2445}`, and Crossref resolves it to Wilson, "Confinement of quarks," Phys. Rev. D 10(8), 2445–2459 (1974). The DOI is stored in lowercase. DOIs are case-insensitive, so the entry was not changed.
- **C03: Tikhonov1952.** Added (see above).
- **C06: GroveKarcher1973 and PennecArsigny2013.** Added.
- **C07: Lojasiewicz1963.** Added.
- **C10: Aumann1976, Jaynes1957 and PennecArsigny2013.** Added, and the PennecArsigny2013 DOI is now confirmed. The notes list "Caticha2015 and JohnsonCaticha2011 metadata fixes" as outstanding, but round 1 already made them (see `bib-keys.md`, corrections 2 and 3). The current entries are the 2012 USP Press monograph and AIP Conf. Proc. 1443, 104–111 (2012), doi 10.1063/1.3703626. Nothing further was needed.
- **C12: Vandergraft1968 and Amari2009alpha.** Added.
- **Pruning notes.** The notes say that some keys are no longer cited: Carr1981; WestHarrison1997, Smith1979 and HintonPoE2002; the C08 list; Pennec2006 and Bhatia2007; Dennis2026metaentropy; Friston2017 and Brown1986. These were not acted on. The bib is shared by several manuscripts and the instructions forbid deletion.

## Unverifiable items

None of the eleven. Two details rest only on secondary sources. The first is the editor and publisher fields of `Lojasiewicz1963`, which come from the C07 log and standard citation practice rather than from zbMATH. The second is the Grove–Karcher and Pennec–Arsigny theorem numbers that the chunk text cites. The chunk panels read those from the papers; this pass verified only bibliographic metadata.

## Checks (executed)

- A parse and uniqueness script (session scratchpad, `val.py`) found 550 entries, balanced braces in every entry, no duplicate keys, no case-only key collisions, CRLF-only line endings, and the pre-edit file as an exact byte prefix.
- BibTeX 0.99d (TeX Live 2025, `unsrt`, `\citation{*}`) formats all 550 entries. It reports the same single pre-existing warning as round 1: "empty journal in Bayne2005".
- `PIFB2.assembled.tex` has 219 distinct cited keys, all defined in the bib, and cites each of the eleven new keys. The C07 citation at the former line 1685 now reads `DorflerBullo2013Kron` (assembled line 1486), so the round-1 action item is resolved in the assembly.
