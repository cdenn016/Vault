# Task 9 independent static proof control

**FINAL: FAIL** (one failing check: SC-5, missing reference targets at LaTeX
semantics. All other checks pass.)

Run date 2026-08-04. Repository
`C:\tmp\Research-gauge-vfe-rg-review-remediation-20260803`, branch
`codex/gauge-vfe-rg-theory-remediation-20260804`,
`HEAD = 3dbe4c610ccc3c0645d25d06ed8fd3074eb4ba3a`, working tree dirty with the
Task 9 edits. All checks are read-only. **No Git mutation and no TeX build was
run.** Every command below is reproducible verbatim from the repository root
unless a different working directory is shown.

Companion mathematical verdict: `evidence/task-9-opus-adversarial.md`.

---

## SC-0. Environment and tool availability

| Tool | Status in this environment |
| --- | --- |
| `git` (read-only: `status`, `diff --stat`, `diff --numstat`, `diff --check`, `blame`) | available |
| `git show` / `git diff` piped / `git diff -S` | **gated by the sandbox**; worked around with `git blame` on the dirty worktree, which distinguishes committed lines from `Not Committed Yet` lines and is strictly more informative for attribution |
| `sha256sum`, `grep` (GNU, with `-P`), `awk`, `sort`, `uniq`, `wc` | available |
| `python` (on `PATH`) | available; used only for JSON parsing and digest recomputation |
| `C:\Python314\python.exe` (the plan's pinned interpreter) | **gated by the sandbox**; substituted by `python` for read-only JSON/digest work |
| `pdflatex` / `bibtex` | not invoked (prohibited by charter) |

---

## SC-1. SHA-256 of every Task 9 file (current bytes)

```
$ cd C:/tmp/Research-gauge-vfe-rg-review-remediation-20260803
$ sha256sum manuscripts/gauge_vfe_rg/07_general_renormalization.tex \
            manuscripts/gauge_vfe_rg/07b_agent_network_rg.tex \
            manuscripts/gauge_vfe_rg/08_infogeometry.tex \
            manuscripts/gauge_vfe_rg/appendix_notation.tex \
            manuscripts/gauge_vfe_rg/appendix_claim_ledger.tex \
            manuscripts/references.bib
```

### Changed sources

| Path | SHA-256 (recomputed) |
| --- | --- |
| `manuscripts/gauge_vfe_rg/07_general_renormalization.tex` | `a3a7ae2fed2eb4a1ea4668393a69b4d56aa2c9dd071af06ddbcba717d7365797` |
| `manuscripts/gauge_vfe_rg/07b_agent_network_rg.tex` | `d4fd13fcdacf464b781456d2388c2521ddafe57418a008e01ce679cf5e57804f` |
| `manuscripts/gauge_vfe_rg/08_infogeometry.tex` | `55bfcdff0eebec24f2231852467255d13a0c02d1369621d04ede53cad3b7c31b` |
| `manuscripts/gauge_vfe_rg/appendix_notation.tex` | `d39936499c9673c1b4ed75ae31bf294f8d4df9fd1fd0cef1dae4a9ec5a572fa4` |
| `manuscripts/gauge_vfe_rg/appendix_claim_ledger.tex` | `bbb02a24ed0875ff287aa072fddae359f4ccd59058157503d4e93502a4e6b436` |
| `manuscripts/references.bib` | `f520c0a7a20e994786e5946f2b6484120d371d8b90a79f37895e22666e93bded` |

### Changed control records

| Path | SHA-256 (recomputed) |
| --- | --- |
| `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/adversarial-report.json` | `873c2675319b7420700abeddc0d6f6ca067bdaab5179b140d1ca3327af9fd77b` |
| `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/approach-registry.json` | `33053bb606eae300359ee33875d892b2c39996aa83fff8a4da5776ea878f4f69` |
| `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/claim-ledger.json` | `7526c443a0f410fe1f8acd9adbcb0e2c1cf4f1be4396290dce89f3fa25af7509` |
| `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/counterexample-register.md` | `5d18bbd4d6887a851bd3b5a660568da2a0b675192ab5f9205ca61138e6d96b34` |
| `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/problem-contract.json` (unchanged, bound) | `a9e1999c85ee333f23a1aacb90a6a51b526565d1e89f958374201a55d06878de` |

### New Task 9 evidence artifacts (untracked)

| Path | SHA-256 (recomputed) |
| --- | --- |
| `evidence/task-9-integrated-proof.md` | `ef88d07ae1c4ff66430c54ed2c691730c56d0af8e04f21007d76608615d53eba` |
| `evidence/task-9-score-dqm-analysis.md` | `78b5b72730fc6ec4a2482137cc9911e9995955c61de74438259ec347e7cb3694` |
| `evidence/task-9-hermite-analysis.md` | `7a94cdf1776d7d7fb88a8672bedd042c739c66b4a5c61e8dcc98f27d1d83beeb` |
| `evidence/task-9-cocycle-beta-analysis.md` | `cca923e14e943680636e9e27e0840385d04587fe1423597ec5e0f376fb3eb267` |
| `evidence/task-9-primary-source-map.md` | `ad0e8102fbee51f0302cd0d05bcf6e019be16d39911da24a2b9d90286a6350e2` |

**Result: PASS** (all digests computed).

---

## SC-2. Verification of the digests claimed in `task-9-integrated-proof.md`

Ten digests are asserted in that record. All ten match the current bytes.

| Asserted at | Path | Match |
| --- | --- | --- |
| Section 3 | `07_general_renormalization.tex` | YES |
| Section 3 | `07b_agent_network_rg.tex` | YES |
| Section 3 | `08_infogeometry.tex` | YES |
| Section 3 | `appendix_notation.tex` | YES |
| Section 3 | `appendix_claim_ledger.tex` | YES |
| Section 3 | `manuscripts/references.bib` | YES |
| Section 2 | `evidence/task-9-score-dqm-analysis.md` | YES |
| Section 2 | `evidence/task-9-hermite-analysis.md` | YES |
| Section 2 | `evidence/task-9-cocycle-beta-analysis.md` | YES |
| Section 2 | `evidence/task-8-independent-reconstruction.md` (`7c0ae6de...1429`) | YES |

The record's claim "all nineteen recorded evidence digests match current bytes"
was also reproduced independently against `claim-ledger.json`:

```
$ cd docs/derivations/2026-08-03-gauge-vfe-rg-remediation
$ python -c "
import json,hashlib,os
d=json.load(open('claim-ledger.json'))
seen={}; bad=0
for e in d['evidence']:
    p=e['artifact_path']; want=e['artifact_sha256']
    got=hashlib.sha256(open(p,'rb').read()).hexdigest()
    if got.lower()!=want.lower(): bad+=1
    seen[p]=got
print('unique artifacts:',len(seen),'mismatches:',bad)"
unique artifacts: 19 mismatches: 0
```

21 evidence entries, 19 unique artifact paths, **0** digest mismatches, **0**
missing files.

**Result: PASS.**

---

## SC-3. JSON parse of every changed / bound control file

```
$ cd docs/derivations/2026-08-03-gauge-vfe-rg-remediation
$ python -c "import json,sys;[print(f,'PARSE_OK',len(json.load(open(f)))) for f in \
  ['adversarial-report.json','approach-registry.json','claim-ledger.json',\
   'problem-contract.json','dependency-dag.json']]"
adversarial-report.json PARSE_OK 8
approach-registry.json  PARSE_OK 8
claim-ledger.json       PARSE_OK 6
problem-contract.json   PARSE_OK 4
dependency-dag.json     PARSE_OK 5
```

`claim-ledger.json` structure: 67 claims, 42 `EVIDENCE_VERIFIED`, 25 `CANDIDATE`,
0 `REFUTED`, 0 `INCONCLUSIVE`. The eight Task 9 claims (`score-dqm-lift`,
`hermite-spectrum`, `generalized-modes`, `cocycle-law`, `fixed-objects`,
`beta-functions`, `jona-lasinio-mapping`, `minor-lumpability-memory-sources`) are
`EVIDENCE_VERIFIED`; all twelve Task 10 claims remain `CANDIDATE`.
`adversarial-report.json.oracle_erasure.result = "NOT_RUN"`.

**Result: PASS.**

---

## SC-4. Duplicate LaTeX labels

```
$ cd manuscripts/gauge_vfe_rg
$ grep -oh -e '\label{[^}]*}' -e 'heading{[^{}]*}{[^{}]*}' *.tex \
  | grep -o '{[^{}]*}$' | sort | uniq -d
(no output)
$ grep -oh -e '\label{[^}]*}' -e 'heading{[^{}]*}{[^{}]*}' *.tex \
  | grep -o '{[^{}]*}$' | sort -u | wc -l
1212
```

24 `.tex` files. **1212** unique label keys, **0** duplicates. Independently
reproduced with an `index()`-based `awk` scanner over the explicit file list
(same 1212). This matches the count asserted at
`evidence/task-9-integrated-proof.md:629-630`.

Extra checks:

* Explicit `\label{...}` alone: 946 unique, `uniq -d` empty.
* Heading-generated labels alone: `uniq -d` empty.
* No cross-collision between the two families (the combined `uniq -d` above).

**Result: PASS.**

---

## SC-5. Missing reference targets

### 5a. String-level check (reproduces the integrated proof's claim)

```
$ cd manuscripts/gauge_vfe_rg
$ awk '{s=$0; while((p=index(s,"label{"))>0){s=substr(s,p+6);q=index(s,"}");
   if(q>0){L[substr(s,1,q-1)]=1;s=substr(s,q+1)}else s=""}
   s=$0; while((p=index(s,"heading{"))>0){s=substr(s,p+8);q=index(s,"}");
   if(q>0){t=substr(s,q+1); if(substr(t,1,1)=="{"){r=index(t,"}");
   if(r>0)L[substr(t,2,r-2)]=1} s=substr(s,q+1)}else s=""}
   s=$0; while((p=index(s,"ref{"))>0){s=substr(s,p+4);q=index(s,"}");
   if(q>0){k=substr(s,1,q-1);n=split(k,a,",");
   for(i=1;i<=n;i++){gsub(/^[ \t]+/,"",a[i]);gsub(/[ \t]+$/,"",a[i]);
   if(a[i]!="")R[a[i]]=1} s=substr(s,q+1)}else s=""}}
   END{nl=0;for(k in L)nl++; nr=0;for(k in R)nr++; miss=0;
   for(k in R) if(!(k in L)){miss++; print "MISSING [" k "]"}
   print "LABELS " nl; print "REFTARGETS " nr; print "MISSING_COUNT " miss}' \
   01_introduction.tex 02_geometry.tex 03_probability.tex 04_generative.tex \
   05_elbo.tex 05a_expfamily.tex 05b_local_collective_elbo.tex \
   05c_pullback_geometry.tex 05d_relational_inference.tex \
   06_general_coarsegraining.tex 06_gaussian.tex 06a_generative_gaussian.tex \
   07_general_renormalization.tex 07_restrictions.tex 07b_agent_network_rg.tex \
   08_infogeometry.tex 09_coarsegraining.tex 10_renormalization.tex \
   11_obstructions.tex 12_philosophy.tex appendix_notation.tex \
   appendix_claim_ledger.tex appendix_numerical_provenance.tex main.tex
LABELS 1212
REFTARGETS 557
MISSING_COUNT 0
```

String level: **557** unique reference targets, **0** unresolved. This exactly
reproduces `evidence/task-9-integrated-proof.md:631-633`.

### 5b. LaTeX-semantics check (this is the failing check)

The string test is not the required test. `manuscripts/gauge_vfe_rg/main.tex:86-100`
defines every `\...heading` wrapper with **two** mandatory arguments, and
`\resultheading` emits `\label{#4}`. Four call sites supply only the title group
on their line and put `\label{key}` on the next line, so TeX takes the control
sequence `\label` itself as `#2`, emits `\label{\label}`, never defines the
intended key, and typesets the trailing brace group as body text.

```
$ cd manuscripts/gauge_vfe_rg
$ grep -rn -A1 'heading{[^{}]*}$' *.tex | grep -v newcommand
07b_agent_network_rg.tex:259:\propositionheading{Bounded recentering gives analyticity at every bounded action}
07b_agent_network_rg.tex-260-\label{prop:rg-action-bounded-recentering}
--
07b_agent_network_rg.tex:1109:\propositionheading{Product equivalence is an admitted, not an automatic, scale premise}
07b_agent_network_rg.tex-1110-\label{prop:rg-product-equivalence-not-preserved}
--
07b_agent_network_rg.tex:1174:\theoremheading{Hoeffding assembly is an exact finite-network action isomorphism}
07b_agent_network_rg.tex-1175-\label{thm:rg-hoeffding-action-isomorphism}
--
07b_agent_network_rg.tex:1243:\propositionheading{Radon--Nikodym covariance of the nonlinear interaction step}
07b_agent_network_rg.tex-1244-\label{prop:rg-interaction-rn-gauge-covariance}
```

No redefinition can rescue these:

```
$ grep -rn -e renewcommand -e providecommand -e DeclareRobustCommand *.tex
appendix_notation.tex:11:\renewcommand{\arraystretch}{1.05}
main.tex:11,13,14 : \chaptermark, \@pnumwidth, \@tocrmarg
main.tex:51-60    : \thedefinition ... \therequirement
```

Dependent reference sites:

```
$ grep -rn 'prop:rg-action-bounded-recentering\|prop:rg-product-equivalence-not-preserved\|thm:rg-hoeffding-action-isomorphism\|prop:rg-interaction-rn-gauge-covariance' *.tex
07b_agent_network_rg.tex:260   \label{prop:rg-action-bounded-recentering}
07b_agent_network_rg.tex:362   \Cref{prop:rg-action-bounded-recentering}
07b_agent_network_rg.tex:1110  \label{prop:rg-product-equivalence-not-preserved}
07b_agent_network_rg.tex:1175  \label{thm:rg-hoeffding-action-isomorphism}
07b_agent_network_rg.tex:1244  \label{prop:rg-interaction-rn-gauge-covariance}
07b_agent_network_rg.tex:1307  \Cref{prop:rg-action-bounded-recentering}
07b_agent_network_rg.tex:1354  \Cref{prop:rg-action-bounded-recentering}
07b_agent_network_rg.tex:1412  \Cref{thm:rg-hoeffding-action-isomorphism}
07b_agent_network_rg.tex:1462  \Cref{prop:rg-interaction-rn-gauge-covariance}
07b_agent_network_rg.tex:2250  \Cref{thm:rg-hoeffding-action-isomorphism}
```

Counts: **4** labels never defined, **6** `\Cref` targets undefined at TeX
semantics, **4** stray label keys typeset as body text.

Attribution (`git blame` on the dirty worktree):

```
$ git blame -L 258,261 -- manuscripts/gauge_vfe_rg/07b_agent_network_rg.tex
3dbe4c61 ... 259) \propositionheading{Bounded recentering ...}
3dbe4c61 ... 260) \label{prop:rg-action-bounded-recentering}
$ git blame -L 1109,1110 -L 1174,1175 -L 1243,1244 -L 1412,1412 -L 2250,2250 -- .../07b_agent_network_rg.tex
3dbe4c61          ... 1109) \propositionheading{Product equivalence ...}
3dbe4c61          ... 1110) \label{prop:rg-product-equivalence-not-preserved}
3dbe4c61          ... 1174) \theoremheading{Hoeffding assembly ...}
3dbe4c61          ... 1175) \label{thm:rg-hoeffding-action-isomorphism}
3dbe4c61          ... 1243) \propositionheading{Radon--Nikodym covariance ...}
3dbe4c61          ... 1244) \label{prop:rg-interaction-rn-gauge-covariance}
00000000 (Not Committed Yet ... 1412) \Cref{thm:rg-hoeffding-action-isomorphism} ...
00000000 (Not Committed Yet ... 2250) inverse identities of \Cref{thm:rg-hoeffding-action-isomorphism} ...
```

All four malformed constructs originate in commit `3dbe4c61` (Task 8). Two of the
six dependent references were added by Task 9's uncommitted edits. All 29 Task 9
heading calls are themselves well formed.

Historical note: the same string-level method was used at the previous
checkpoints and also missed this class:
`evidence/task-7-static-proof-control.md:34` reports 1,086 labels and
`evidence/task-8-static-proof-control.md:35` reports 1,118, both with no finding.

**Result: FAIL.** Detail and minimal repair: `evidence/task-9-opus-adversarial.md`, B-1.

---

## SC-6. Bibliography: cited keys, undefined keys, duplicate keys

```
$ cd manuscripts
$ grep -cE '^@[A-Za-z]+\{[^,]+,' references.bib
464
$ grep -oE '^@[A-Za-z]+\{[^,]+,' references.bib | sort | uniq -d
(no output)
$ awk '/^@/{p=index($0,"{");q=index($0,",");
   if(p>0&&q>p){k=substr($0,p+1,q-p-1);gsub(/[ \t]/,"",k);C[k]++;D[tolower(k)]++}}
   END{n=0;d=0;cd=0;for(k in C){n++;if(C[k]>1){d++;print "DUPKEY " k}}
   for(k in D) if(D[k]>1){cd++; print "DUPKEY_CI " k}
   print "BIBKEYS " n; print "EXACT_DUPS " d; print "CASEINSENS_DUPS " cd}' references.bib
BIBKEYS 464
EXACT_DUPS 0
CASEINSENS_DUPS 0
```

Cited-versus-defined (two-file `awk` pass over `references.bib` plus all 24
manuscript `.tex` files, cite scanner skipping trailing letters and optional
`[...]` groups so prose occurrences of "cite" are ignored):

```
BIBKEYS       464
CITED_UNIQUE   79
UNDEFINED       0
```

This reproduces `evidence/task-9-integrated-proof.md:634-638` exactly.

Task 9 source entries present and metadata-consistent with the audited publisher
records:

| Key | Line | Key fields |
| --- | --- | --- |
| `JonaLasinio2001` | `references.bib:1103` | Physics Reports 352(4--6) 439--458; DOI `10.1016/S0370-1573(01)00042-4`; eprint `cond-mat/0009219`; `archivePrefix=arXiv`; `primaryClass=cond-mat.stat-mech` |
| `KemenySnell1976` | `references.bib:1117` | Springer, New York, 1976; UTM; note "Reprint of the 1960 Van Nostrand edition" |
| `Nakajima1958` | `references.bib:1127` | Prog. Theor. Phys. 20(6) 948--959; DOI `10.1143/PTP.20.948` |
| `Zwanzig1960` | `references.bib:1138` | J. Chem. Phys. 33(5) 1338--1341; DOI `10.1063/1.1731409` |
| `Arnold1998` | `references.bib:1149` | Springer Monographs in Mathematics, Berlin, 1998; ISBN `3-540-63758-3` |

Two title fields are abbreviated relative to
`evidence/task-9-primary-source-map.md:299-300` (`Nakajima1958` drops the
subtitle "Steady Diffusion"; `KemenySnell1976` uses the short title). Recorded as
non-blocking finding N-3.

Citation sites, all five at the narrowed scope:
`07:735` (`Arnold1998`, inside `NOT-CLAIMED`), `07b:976` and `07b:982`
(`JonaLasinio2001`), `07b:1965` (`\citet[Ch.~6]{KemenySnell1976}`), `07b:2058`
(`Nakajima1958`, `Zwanzig1960`).

**Result: PASS.**

---

## SC-7. `git diff --check`

```
$ cd C:/tmp/Research-gauge-vfe-rg-review-remediation-20260803
$ git diff --check ; echo "exit=$?"
warning: in the working copy of 'docs/.../adversarial-report.json', LF will be replaced by CRLF ...
warning: in the working copy of 'docs/.../approach-registry.json', LF will be replaced by CRLF ...
warning: in the working copy of 'docs/.../claim-ledger.json', LF will be replaced by CRLF ...
warning: in the working copy of 'docs/.../counterexample-register.md', LF will be replaced by CRLF ...
exit=0
```

Zero whitespace errors. The four messages are `core.autocrlf` advisories, not
`--check` findings. Direct confirmation over the six changed sources:

```
$ grep -nP '[ \t]+$|\t| $' <the six changed source files>
(no output)
```

Zero blank-at-EOL, zero space-before-tab, zero tabs. No blank-at-EOF (the last
line of `07b_agent_network_rg.tex` is line 2749 and is non-blank).

**Result: PASS.** (This closes the limitation recorded at
`evidence/task-9-integrated-proof.md:647-651`, which reported that `git diff --check`
could not be executed in the integration environment. It runs here and is clean.)

---

## SC-8. Encoding, placeholders, spelling

```
$ grep -nP '[^\x00-\x7F]' manuscripts/gauge_vfe_rg/07_general_renormalization.tex \
    manuscripts/gauge_vfe_rg/07b_agent_network_rg.tex \
    manuscripts/gauge_vfe_rg/08_infogeometry.tex \
    manuscripts/gauge_vfe_rg/appendix_notation.tex \
    manuscripts/gauge_vfe_rg/appendix_claim_ledger.tex
(no output)

$ grep -nP '[^\x00-\x7F]' manuscripts/references.bib
1684:  editor = {Brüntrup, Godehard and Jaskolla, Ludwig},
2156:% Čencov - uniqueness of Fisher-Rao metric
2178:  note = {Alternative spelling: Čencov. ...}
```

Non-ASCII in the five TeX files: **0**. In `references.bib`: **3** legitimate
diacritics (one u-umlaut, two c-hacek) at the three pre-existing lines named in
`evidence/task-9-integrated-proof.md:620-623`. **No mojibake sequence anywhere.**

```
$ grep -nEi '\b(TODO|TBD|FIXME|XXX|placeholder|to be determined|left to the reader|\
    it is well known|straightforward(ly)? (to see|check)|clearly|obviously|trivially|routine)\b' \
    <the five changed TeX files>
(no output)

$ grep -nEi '\b(behaviour|colour|normalis|generalis|characteris|realis|parametris|\
    neighbourhood|centre|analyse|labelled|modelling|favour|rigour|summaris|minimis|\
    maximis|utilis|specialis|orthogonalis|diagonalis|factoris|discretis|linearis|\
    renormalis|marginalis|axiomatis|regularis|symmetris)[a-z]*' <the five changed TeX files>
(no output)
```

Placeholder/hedge hits: **0**. British spellings: **0**.

Environment nesting (`awk`, per file, per environment name):

```
IMBALANCES 0
```

Zero `\begin`/`\end` imbalances and zero orphan `\end` across the five changed
TeX files.

Status tags in the five changed TeX files:

```
$ grep -oh 'status{[^}]*}' <the five changed TeX files> | sort | uniq -c | sort -rn
    129 status{ESTABLISHED}
     34 status{OPEN}
     26 status{DEFINITION}
      8 status{NOT-CLAIMED}
      6 status{HYPOTHESIS}
      3 status{NUMERICAL}
      1 status{CONJECTURE}
```

Doubled `\status` on one physical line:

```
$ grep -cn 'status{[^}]*}.*status{' <the five changed TeX files>
07_general_renormalization.tex:0
07b_agent_network_rg.tex:0
08_infogeometry.tex:3
appendix_notation.tex:0
appendix_claim_ledger.tex:0
```

Three occurrences, at `08_infogeometry.tex:503,529,543`, all inside
`sec:ig-notclaimed` (which begins at `:491`), all pre-existing by `git blame`
(`a2cca53b`, `96b7b5f6`, `0af1cbd3`), none introduced by Task 9. See non-blocking
finding N-5 for one inaccurate characterization of line 543 in
`evidence/task-9-integrated-proof.md:642-645`.

All three `\status{NUMERICAL}` occurrences (`08_infogeometry.tex:195,334,488`) are
pre-existing and each is explicitly self-limiting ("not a proof" / "Computation is
not proof and the proof is above"). No numerical result is presented as proof.

**Result: PASS.**

---

## SC-9. Protected files and touched-file scope

```
$ git status --short
 M docs/derivations/2026-08-03-gauge-vfe-rg-remediation/adversarial-report.json
 M docs/derivations/2026-08-03-gauge-vfe-rg-remediation/approach-registry.json
 M docs/derivations/2026-08-03-gauge-vfe-rg-remediation/claim-ledger.json
 M docs/derivations/2026-08-03-gauge-vfe-rg-remediation/counterexample-register.md
 M manuscripts/gauge_vfe_rg/07_general_renormalization.tex
 M manuscripts/gauge_vfe_rg/07b_agent_network_rg.tex
 M manuscripts/gauge_vfe_rg/08_infogeometry.tex
 M manuscripts/gauge_vfe_rg/appendix_claim_ledger.tex
 M manuscripts/gauge_vfe_rg/appendix_notation.tex
 M manuscripts/references.bib
?? .verification/active.json
?? .verification/task1-proof-control-ledger.json
?? .verification/task3-factorization-closure-ledger.json
?? docs/derivations/.../evidence/task-9-cocycle-beta-analysis.md
?? docs/derivations/.../evidence/task-9-hermite-analysis.md
?? docs/derivations/.../evidence/task-9-integrated-proof.md
?? docs/derivations/.../evidence/task-9-primary-source-map.md
?? docs/derivations/.../evidence/task-9-score-dqm-analysis.md
```

### Protected files

| Path | Git state | SHA-256 |
| --- | --- | --- |
| `.verification/active.json` | **untracked (`??`), unmodified** | `3c9b6a7e0cfc3bff87546f3de2f06947a5d8b6025475d4580197997890763a32` |
| `.verification/task1-proof-control-ledger.json` | **untracked (`??`), unmodified** | `baf813f207c353fd8fe3c97508e50216771efc84ad9533cd91297b22b6309a5d` |
| `.verification/task3-factorization-closure-ledger.json` | **untracked (`??`), unmodified** | `3a1eb77de7c8f561cf9b3658ace4f88ed63b017fb283a2a72a0f06da2791ec78` |
| `manuscripts/gauge_vfe_rg/verification/current-results.json` | **not in `git status`: unmodified and committed** | `71e58869e3fb7f0f04c506f74542eb3603fa156781e82755162f2f5a1a7ce893` |

All three `.verification` files remain untracked and unmodified. Neither
`current-results.json` nor anything under `manuscripts/gauge_vfe_rg/verification/`
appears in the change set.

### Scope

```
$ git diff --numstat
15   10  docs/.../adversarial-report.json
68   13  docs/.../approach-registry.json
14    9  docs/.../claim-ledger.json
17    3  docs/.../counterexample-register.md
269   0  manuscripts/gauge_vfe_rg/07_general_renormalization.tex
1062 25  manuscripts/gauge_vfe_rg/07b_agent_network_rg.tex
76    0  manuscripts/gauge_vfe_rg/08_infogeometry.tex
41    0  manuscripts/gauge_vfe_rg/appendix_claim_ledger.tex
74    0  manuscripts/gauge_vfe_rg/appendix_notation.tex
53    6  manuscripts/references.bib
```

Ten modified paths, five new untracked evidence files. Every one is inside the
Task 9 file map declared by the plan
(`docs/superpowers/plans/2026-08-03-gauge-vfe-rg-review-remediation.md`, Task 9:
"Modify `07_general_renormalization.tex`, `07b_agent_network_rg.tex`,
`08_infogeometry.tex`, appendices, bibliography, and proof artifacts"). No TeX
file outside the declared set, no verifier source, no test, no build script, no
schema, no wiki file, and no generated result is touched.

**Result: PASS.**

---

## SC-10. Digest binding of the new evidence artifacts

Four of the five new Task 9 evidence artifacts are digest-bound by
`claim-ledger.json` (SC-2). The fifth,
`evidence/task-9-primary-source-map.md`
(`ad0e8102fbee51f0302cd0d05bcf6e019be16d39911da24a2b9d90286a6350e2`), appears in
**no** control record: not in `claim-ledger.json.evidence`, not in
`adversarial-report.json`, and not in `evidence/task-9-integrated-proof.md`
Section 2 or Section 3. Recorded as non-blocking finding N-4 in the adversarial
report.

**Result: PASS with observation.**

---

## Summary table

| ID | Check | Result |
| --- | --- | --- |
| SC-1 | SHA-256 of every Task 9 changed source, control, and evidence file | PASS |
| SC-2 | Digests asserted in `task-9-integrated-proof.md` (10/10) and in `claim-ledger.json` (19 artifacts, 0 mismatches) | PASS |
| SC-3 | JSON parse of all five control files; ledger state census | PASS |
| SC-4 | Duplicate LaTeX labels: 1212 unique, 0 duplicates | PASS |
| SC-5 | **Missing reference targets: 0 at string level, 6 at LaTeX semantics across 4 never-defined labels** | **FAIL** |
| SC-6 | Bibliography: 464 keys, 0 duplicates (exact and case-insensitive), 79 cited, 0 undefined | PASS |
| SC-7 | `git diff --check` exit 0; direct whitespace scan clean | PASS |
| SC-8 | Encoding (0 non-ASCII in TeX, 3 legitimate diacritics in `.bib`), 0 placeholders, 0 British spellings, 0 environment imbalances, status-tag census | PASS |
| SC-9 | Three `.verification` files untracked and unmodified; `current-results.json` unmodified; touched-file scope matches the plan's Task 9 map | PASS |
| SC-10 | Evidence digest binding; one unbound artifact recorded | PASS with observation |

**FINAL: FAIL** on SC-5. Nine of ten checks pass. The single failure is
mechanical, has an exact four-line repair, and is documented as blocker B-1 in
`evidence/task-9-opus-adversarial.md`.
