# Task 9 heading repair: closure record for blocker B-1

**FINAL: PASS.** The single blocker returned by the independent Task 9 audit is
repaired, and every check re-run over the repaired bytes passes. No check beyond
B-1 failed, so no blocker is recorded in section 12.

Run date 2026-08-04. Repository
`C:\tmp\Research-gauge-vfe-rg-review-remediation-20260803`, branch
`codex/gauge-vfe-rg-theory-remediation-20260804`,
`HEAD = 3dbe4c610ccc3c0645d25d06ed8fd3074eb4ba3a`, working tree dirty with the
Task 9 edits. Interpreter `C:\Python314\python.exe`, Python 3.14.4, which is the
plan's pinned interpreter and is what `python` resolves to on `PATH` here. All
checks are read-only apart from the four source lines named in section 3 and the
records named in section 11. **No Git mutation and no TeX build was run.**

## 0. Scope and authority

This pass repairs **B-1 only**, exactly as prescribed by the audit's minimal
repair. It changes no theorem statement, no proof, no equation, no notation, no
citation, and no status tag. The two independent audit reports are **not edited**
and stand as the historical falsification evidence:

| Report | SHA-256 (unchanged) | Verdict recorded there |
| --- | --- | --- |
| `evidence/task-9-opus-adversarial.md` | `75fb7674319a0a20f338c648669ab148ae20f4c7186bbe6ab8808744415f97fe` | **FAIL** on one blocker, B-1; **no mathematical blocker** |
| `evidence/task-9-static-proof-control.md` | `f7045145725357ccb1eb52f0358e27e7c48b2fc47b3ad000ebdfcc53218ec5c9` | **FAIL** on check SC-5; nine of ten checks pass |

**No circular hash dependency.** This record binds the integrated proof and the
control records by digest. None of those files binds this record by digest:
`evidence/task-9-integrated-proof.md` cites this artifact by path only, and the
audit-trail entry added to `approach-registry.json` names it by path only. The
dependency runs one way.

## 1. Revision binding: pre- and post-repair digests

| Path | Pre-repair SHA-256 | Post-repair SHA-256 |
| --- | --- | --- |
| `manuscripts/gauge_vfe_rg/07b_agent_network_rg.tex` | `d4fd13fcdacf464b781456d2388c2521ddafe57418a008e01ce679cf5e57804f` | `148d9652229eb6d3c40a41b48c1eb938328ca697a37e8113111567c580cc61be` |
| `evidence/task-9-integrated-proof.md` | `ef88d07ae1c4ff66430c54ed2c691730c56d0af8e04f21007d76608615d53eba` | `7bd7391ccbe163797a68433b06729cfc956da6cd40af5436168fe0b7a9aa640f` |
| `claim-ledger.json` | `7526c443a0f410fe1f8acd9adbcb0e2c1cf4f1be4396290dce89f3fa25af7509` | `effb5663af4e51339464f1765185fb0c35d767b9141614a7f3b0fe28a33099d3` |
| `adversarial-report.json` | `873c2675319b7420700abeddc0d6f6ca067bdaab5179b140d1ca3327af9fd77b` | `724442daa743b8910f86eea377be7afd3347481af8ba08ed5c7b1f171259db32` |
| `approach-registry.json` | `33053bb606eae300359ee33875d892b2c39996aa83fff8a4da5776ea878f4f69` | `2f91d81fadf7e2678963e6247067933417701938aa173de301fe604d49907430` |

The five pre-repair digests were recomputed from disk before any edit and agree
with the values independently recorded in `evidence/task-9-static-proof-control.md`
section SC-1, so this pass started from exactly the bytes the audit examined.

Unchanged and re-verified at the close of the pass:

| Path | SHA-256 | Status |
| --- | --- | --- |
| `counterexample-register.md` | `5d18bbd4d6887a851bd3b5a660568da2a0b675192ab5f9205ca61138e6d96b34` | not edited; matches SC-1 |
| `evidence/task-9-opus-adversarial.md` | `75fb7674...415f97fe` | not edited |
| `evidence/task-9-static-proof-control.md` | `f7045145...218ec5c9` | not edited |
| `.verification/active.json` | `3c9b6a7e0cfc3bff87546f3de2f06947a5d8b6025475d4580197997890763a32` | untracked, unmodified |
| `.verification/task1-proof-control-ledger.json` | `baf813f207c353fd8fe3c97508e50216771efc84ad9533cd91297b22b6309a5d` | untracked, unmodified |
| `.verification/task3-factorization-closure-ledger.json` | `3a1eb77de7c8f561cf9b3658ace4f88ed63b017fb283a2a72a0f06da2791ec78` | untracked, unmodified |
| `manuscripts/gauge_vfe_rg/verification/current-results.json` | `71e58869e3fb7f0f04c506f74542eb3603fa156781e82755162f2f5a1a7ce893` | committed, unmodified |

## 2. The defect, and why the published check could not see it

`manuscripts/gauge_vfe_rg/main.tex:86-100` defines every result heading through a
single four-argument primitive and ten two-argument wrappers:

```latex
\newcommand{\resultheading}[4]{%
  \syncstatementcounter{#2}%
  \label{#4}%
  \paragraph{#1~\csname the#2\endcsname\ (#3).}%
}
\newcommand{\propositionheading}[2]{\resultheading{Proposition}{proposition}{#1}{#2}}
\newcommand{\theoremheading}[2]{\resultheading{Theorem}{theorem}{#1}{#2}}
```

Each wrapper therefore takes **two mandatory arguments**, and the second is the
label key. Four call sites in `07b_agent_network_rg.tex` supplied only the title
group on the macro's line and placed `\label{key}` on the next line. TeX scans an
undelimited argument by skipping space tokens, including the one produced by the
end of line, and then taking the next token. That token is the control sequence
`\label` itself, not a brace group. So `#2` became `\label`, the wrapper expanded
to `\label{\label}`, the intended key was never passed to `\label`, and the
trailing brace group was left in the input stream and typeset as body text.

The result is four labels TeX never defines and six `\Cref` sites that resolve to
nothing. Nothing rescues this: across `manuscripts/gauge_vfe_rg/*.tex` the only
`\renewcommand` uses are `\arraystretch`, `\chaptermark`, `\@pnumwidth`,
`\@tocrmarg`, and the ten `\the<counter>` redefinitions, there is no
`\providecommand` or `\DeclareRobustCommand` touching the heading macros, and
there is no `.sty` in the directory that redefines them.

The check published at `evidence/task-9-integrated-proof.md:631-633` matched the
literal strings `\label{...}` and `heading{...}{...}` and reported 557 targets
with zero unresolved. That is a statement about source text, not about the
document TeX produces. Section 5.3 shows it returns identical numbers before and
after the repair, so it could not have detected this defect class in either
direction.

## 3. The exact changed lines

Four line joins in `manuscripts/gauge_vfe_rg/07b_agent_network_rg.tex`. Nothing
else in the file changed.

| Before (two lines) | After (one line) |
| --- | --- |
| `259`, `260` | `259` |
| `1109`, `1110` | `1108` |
| `1174`, `1175` | `1172` |
| `1243`, `1244` | `1240` |

**Before:**

```latex
259 | \propositionheading{Bounded recentering gives analyticity at every bounded action}
260 | \label{prop:rg-action-bounded-recentering}

1109 | \propositionheading{Product equivalence is an admitted, not an automatic, scale premise}
1110 | \label{prop:rg-product-equivalence-not-preserved}

1174 | \theoremheading{Hoeffding assembly is an exact finite-network action isomorphism}
1175 | \label{thm:rg-hoeffding-action-isomorphism}

1243 | \propositionheading{Radon--Nikodym covariance of the nonlinear interaction step}
1244 | \label{prop:rg-interaction-rn-gauge-covariance}
```

**After:**

```latex
 259 | \propositionheading{Bounded recentering gives analyticity at every bounded action}{prop:rg-action-bounded-recentering}
1108 | \propositionheading{Product equivalence is an admitted, not an automatic, scale premise}{prop:rg-product-equivalence-not-preserved}
1172 | \theoremheading{Hoeffding assembly is an exact finite-network action isomorphism}{thm:rg-hoeffding-action-isomorphism}
1240 | \propositionheading{Radon--Nikodym covariance of the nonlinear interaction step}{prop:rg-interaction-rn-gauge-covariance}
```

The repaired lines are 118, 131, 118, and 121 characters. The manuscript has no
line-length rule: `SPEC.md` imposes none, 379 lines across the twenty-four TeX
files already exceed 120 characters, and the longest is 1519. The label keys keep
the `prop:` and `thm:` prefixes that `SPEC.md` section 4 requires.

## 4. Proof that nothing else in the source changed

Two independent mechanical confirmations.

**Byte-level reconstruction.** Undoing exactly the four joins in the current
bytes, that is, rewriting each `}{key}` back to `}` + CRLF + `\label{key}`,
reproduces the audited pre-repair digest exactly:

```
reconstructed-pre  sha256 d4fd13fcdacf464b781456d2388c2521ddafe57418a008e01ce679cf5e57804f
audit-recorded pre sha256 d4fd13fcdacf464b781456d2388c2521ddafe57418a008e01ce679cf5e57804f
MATCH: True
```

Since SHA-256 preimages are not available to a repair pass, this establishes that
the working-tree file differs from the audited file in exactly those four joins
and in nothing else.

**Structural accounting.** The file lost 32 bytes, which is `4 x 8`: each site
removes one CRLF, `\label{` and one `}`, and adds `{` and `}`, for a net of eight
bytes. Physical lines fell from 2749 to 2745. Line endings remain uniformly CRLF
(2745 CRLF, zero bare LF), the trailing newline is preserved, and there are zero
trailing-whitespace lines, zero tabs, and zero non-ASCII characters.
`git diff --numstat` for the file moved from `1062 25` to `1066 33` against
`HEAD`, which is exactly four lines added and eight removed.

## 5. The semantic-aware heading-arity and label check

### 5.1 The scanner

Save as `check_heading_semantics.py` in the repository root and run
`python check_heading_semantics.py`. It models TeX argument scanning rather than
matching strings. Brace, backslash, and newline characters are bound to named
constants via `chr`, so the program survives transmission through shells that
rewrite backslash escapes; saving and running it produces identical output to the
inline invocation used here.

```python
import os, bisect
D = os.path.join("manuscripts", "gauge_vfe_rg")
LB, RB, BS = chr(123), chr(125), chr(92)
W = ("definitionheading lemmaheading propositionheading theoremheading "
     "corollaryheading conjectureheading openproblemheading hypothesisheading "
     "constructionheading requirementheading").split()
AR = dict((w, 2) for w in W); AR["resultheading"] = 4
R1 = set("ref Cref cref eqref autoref pageref nameref namecref labelcref vref Vref".split())
R2 = set("Crefrange crefrange".split())
DEF = set("newcommand renewcommand providecommand DeclareRobustCommand".split())
LET = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
def scan(t, f):
    n = len(t); st = [0] + [i+1 for i, c in enumerate(t) if c == chr(10)]
    labs, refs, heads, errs = [], [], [], []
    def ln(i): return bisect.bisect_right(st, i)
    def cs(i):
        j = i+1
        if j < n and t[j] in LET:
            k = j
            while k < n and t[k] in LET: k += 1
            return t[j:k], k
        return (t[j:j+1] if j < n else ""), min(j+1, n)
    def skip(i):
        nl = 0; par = False
        while i < n:
            c = t[i]
            if c == chr(10):
                nl += 1
                if nl >= 2: par = True
                i += 1
            elif c in " " + chr(9) + chr(13): i += 1
            elif c == "%":
                while i < n and t[i] != chr(10): i += 1
            else: break
        return i, par
    def grp(i):
        if i >= n or t[i] != LB: return None
        d = 0; j = i; out = []
        while j < n:
            c = t[j]
            if c == BS and j+1 < n: out.append(t[j:j+2]); j += 2; continue
            if c == LB:
                d += 1
                if d > 1: out.append(c)
                j += 1; continue
            if c == RB:
                d -= 1
                if d == 0: return "".join(out), j+1
                out.append(c); j += 1; continue
            out.append(c); j += 1
        return None
    def tok(i):
        if i >= n: return "", i
        if t[i] == BS:
            nm, j = cs(i); return BS+nm, j
        return t[i], i+1
    def opts(i):
        while True:
            i, _ = skip(i)
            if i < n and t[i] == "*": i += 1; continue
            if i < n and t[i] == "[":
                d = 0; j = i
                while j < n:
                    if t[j] == "[": d += 1
                    elif t[j] == "]":
                        d -= 1
                        if d == 0: j += 1; break
                    j += 1
                i = j; continue
            return i
    def skipdef(i):
        i = opts(i); g = grp(i)
        if g is not None: i = g[1]
        elif i < n and t[i] == BS: _, i = cs(i)
        i = opts(i); i, _ = skip(i); g = grp(i)
        return g[1] if g is not None else i
    i = 0
    while i < n:
        c = t[i]
        if c == "%":
            while i < n and t[i] != chr(10): i += 1
            continue
        if c != BS: i += 1; continue
        nm, j = cs(i); L = ln(i)
        if nm in DEF: i = skipdef(j)
        elif nm in AR:
            a = AR[nm]; args = []; bad = []; par = False; i = j
            for k in range(a):
                i, p = skip(i); par = par or p
                g = grp(i)
                if g is not None: args.append(("group", g[0])); i = g[1]
                else:
                    tk, i = tok(i); args.append(("token", tk)); bad.append(k+1)
            ok = (not bad) and (not par)
            heads.append((f, L, nm, a, args, bad, par, ok))
            if ok: labs.append((args[a-1][1].strip(), f, L, "heading"))
        elif nm == "label":
            j2, _ = skip(j); g = grp(j2)
            if g is None: errs.append(("label-without-group", f, L)); i = j
            else: labs.append((g[0].strip(), f, L, "explicit")); i = g[1]
        elif nm in R1 or nm in R2:
            k = opts(j); g = grp(k)
            if g is None: errs.append(("ref-without-group", f, L)); i = j
            else:
                for q in g[0].split(","):
                    if q.strip(): refs.append((q.strip(), f, L, nm))
                i = g[1]
                if nm in R2:
                    k2, _ = skip(i); g2 = grp(k2)
                    if g2 is not None:
                        for q in g2[0].split(","):
                            if q.strip(): refs.append((q.strip(), f, L, nm))
                        i = g2[1]
        else: i = j
    return labs, refs, heads, errs
files = sorted(x for x in os.listdir(D) if x.endswith(".tex"))
L, R, H, E = [], [], [], []
for f in files:
    fh = open(os.path.join(D, f), "r", encoding="utf-8", newline=""); s = fh.read(); fh.close()
    a, b, c, d = scan(s, f); L += a; R += b; H += c; E += d
print("FILES SCANNED             %d" % len(files))
print("HEADING CALL SITES        %d" % len(H))
for m in sorted(set(h[2] for h in H)):
    sub = [h for h in H if h[2] == m]
    print("   %-22s %4d   well-formed %4d   malformed %d"
          % (m, len(sub), sum(1 for h in sub if h[7]), sum(1 for h in sub if not h[7])))
bad = [h for h in H if not h[7]]
print("MALFORMED HEADING CALLS   %d" % len(bad))
for h in bad:
    print("   !! %s:%d  %s  bad-arg-positions=%s  par=%s  args=%s"
          % (h[0], h[1], h[2], h[5], h[6], [(u, v[:56]) for u, v in h[4]]))
keys = [k for k, _, _, _ in L]; uniq = set(keys)
dups = sorted(set(k for k in keys if keys.count(k) > 1))
print("LABELS DEFINED (semantic) total %d   unique %d   duplicates %d" % (len(keys), len(uniq), len(dups)))
print("   from heading macros    %d" % sum(1 for x in L if x[3] == "heading"))
print("   from explicit label    %d" % sum(1 for x in L if x[3] == "explicit"))
for d in dups: print("   !! DUPLICATE %s" % d)
rk = sorted(set(k for k, _, _, _ in R))
print("REFERENCE MACROS USED:")
for m in sorted(set(x[3] for x in R)):
    print("   %-12s %4d occurrences" % (m, sum(1 for x in R if x[3] == m)))
print("REFERENCE TARGETS total %d   unique %d" % (len(R), len(rk)))
unres = [k for k in rk if k not in uniq]
print("UNRESOLVED TARGETS        %d" % len(unres))
for u in unres:
    print("   !! UNRESOLVED %s  <- %s" % (u, [(x[1], x[2], x[3]) for x in R if x[0] == u]))
print("SCANNER ERRORS            %d" % len(E))
for e in E: print("   !! %s" % (e,))
print("VERDICT %s" % ("PASS" if not bad and not dups and not unres and not E else "FAIL"))
```

The decision rule it implements:

* a control word is a backslash followed by letters; a control symbol is a
  backslash followed by one non-letter character;
* before each mandatory argument, space tokens, a single end-of-line, and
  percent-comments are skipped, and a blank line is flagged as `\par`, which is
  not a space token;
* a mandatory argument is the next **brace group**, and otherwise the single next
  **token**, which is precisely the rule that lets a stray `\label` be eaten;
* `\newcommand`-family bodies are skipped wholesale, so macro definitions are
  never counted as call sites and the `\label{#4}` inside `\resultheading` is
  never counted as a document label;
* a heading call passes only when **every** mandatory argument is a brace group,
  and only then does its last argument enter the defined-label set.

All ten wrappers plus `\resultheading` are scanned, not only the four macros
named in the blocker, so the check covers the whole family.

### 5.2 Results before and after

Both runs cover all twenty-four files in `manuscripts/gauge_vfe_rg/`.

**Before the repair:**

```
FILES SCANNED             24
HEADING CALL SITES        260
   conjectureheading         1   well-formed    1   malformed 0
   constructionheading       1   well-formed    1   malformed 0
   corollaryheading         24   well-formed   24   malformed 0
   definitionheading        48   well-formed   48   malformed 0
   hypothesisheading        20   well-formed   20   malformed 0
   lemmaheading              1   well-formed    1   malformed 0
   openproblemheading        4   well-formed    4   malformed 0
   propositionheading      116   well-formed  113   malformed 3
   requirementheading        1   well-formed    1   malformed 0
   theoremheading           44   well-formed   43   malformed 1
MALFORMED HEADING CALLS   4
   !! 07b_agent_network_rg.tex:259   propositionheading  bad-arg-positions=[2]  args=[('group', 'Bounded recentering ...'), ('token', '\label')]
   !! 07b_agent_network_rg.tex:1109  propositionheading  bad-arg-positions=[2]  args=[('group', 'Product equivalence ...'),  ('token', '\label')]
   !! 07b_agent_network_rg.tex:1174  theoremheading      bad-arg-positions=[2]  args=[('group', 'Hoeffding assembly ...'),   ('token', '\label')]
   !! 07b_agent_network_rg.tex:1243  propositionheading  bad-arg-positions=[2]  args=[('group', 'Radon--Nikodym covariance ...'), ('token', '\label')]
LABELS DEFINED (semantic) total 1197   unique 1197   duplicates 0
   from heading macros    256
   from explicit label    941
UNRESOLVED TARGETS        3
   !! prop:rg-action-bounded-recentering       <- 07b:362, 07b:1307, 07b:1354  (Cref)
   !! prop:rg-interaction-rn-gauge-covariance  <- 07b:1462                     (Cref)
   !! thm:rg-hoeffding-action-isomorphism      <- 07b:1412, 07b:2250           (Cref)
SCANNER ERRORS            0
VERDICT FAIL
```

**After the repair:**

```
FILES SCANNED             24
HEADING CALL SITES        260
   conjectureheading         1   well-formed    1   malformed 0
   constructionheading       1   well-formed    1   malformed 0
   corollaryheading         24   well-formed   24   malformed 0
   definitionheading        48   well-formed   48   malformed 0
   hypothesisheading        20   well-formed   20   malformed 0
   lemmaheading              1   well-formed    1   malformed 0
   openproblemheading        4   well-formed    4   malformed 0
   propositionheading      116   well-formed  116   malformed 0
   requirementheading        1   well-formed    1   malformed 0
   theoremheading           44   well-formed   44   malformed 0
MALFORMED HEADING CALLS   0
LABELS DEFINED (semantic) total 1201   unique 1201   duplicates 0
   from heading macros    260
   from explicit label    941
REFERENCE MACROS USED:
   Cref          383 occurrences
   eqref         638 occurrences
   ref            43 occurrences
REFERENCE TARGETS total 1064   unique 557
UNRESOLVED TARGETS        0
SCANNER ERRORS            0
REPAIRED KEY prop:rg-action-bounded-recentering             defined-by [('07b_agent_network_rg.tex', 259, 'heading')]
REPAIRED KEY prop:rg-product-equivalence-not-preserved      defined-by [('07b_agent_network_rg.tex', 1108, 'heading')]
REPAIRED KEY thm:rg-hoeffding-action-isomorphism            defined-by [('07b_agent_network_rg.tex', 1172, 'heading')]
REPAIRED KEY prop:rg-interaction-rn-gauge-covariance        defined-by [('07b_agent_network_rg.tex', 1240, 'heading')]
VERDICT PASS
```

Four undefined labels produced only three unresolved keys because
`prop:rg-product-equivalence-not-preserved` has no reference site. Six reference
sites were affected, matching the audit's B-1 table exactly.

The explicit-label count is 941 in both runs, which is itself a check on the
scanner: before the repair the four `\label` control sequences were consumed as
heading arguments and so were correctly **not** counted as explicit labels, and
after the repair those four lines no longer exist.

### 5.3 Reconciliation against the retired string-level scan

The string-level method matched `label{...}` and `heading{...}{...}` and split
`ref{...}` on commas, reproducing the awk pipeline of
`evidence/task-9-static-proof-control.md` section SC-5a. Run over both states:

```
PRE   string-level unique labels 1212   unique ref targets 557   string-level unresolved 0
POST  string-level unique labels 1212   unique ref targets 557   string-level unresolved 0
string-level label set identical PRE vs POST: True
the four disputed keys present in string-level set PRE: True
```

The string-level label **set** is byte-identical before and after the repair, so
that check is provably blind to this defect class in both directions. Its 1212
decomposes exactly:

* `1201` labels that TeX actually defines, plus
* `11` keys that are not labels at all, all read out of `main.tex` definition
  bodies: `#4` from the `\label{#4}` inside `\resultheading`, and the ten counter
  names `definition`, `lemma`, `proposition`, `theorem`, `corollary`,
  `conjecture`, `openproblem`, `hypothesis`, `construction`, `requirement`,
  captured as the second group of each `\newcommand` wrapper body.

Before the repair the same 1212 was `1197 + 11 + 4`, the last four being keys the
string method credited but TeX never defines. Both arithmetics close exactly, so
the 1212 figure is fully explained and the discrepancy is not residual.

## 6. Reference counts

| Quantity | Before | After |
| --- | --- | --- |
| Reference sites (`\Cref`, `\ref`, `\eqref`) | 1064 | 1064 |
| `\Cref` occurrences | 383 | 383 |
| `\eqref` occurrences | 638 | 638 |
| `\ref` occurrences | 43 | 43 |
| Unique reference targets | 557 | 557 |
| Unresolved targets at LaTeX semantics | **3 keys over 6 sites** | **0** |

No `\cref`, `\autoref`, `\pageref`, `\nameref`, `\namecref`, `\labelcref`,
`\vref`, `\Vref`, `\crefrange`, or `\Crefrange` occurs in the manuscript; the
scanner searches for all of them and found none, so the target set is complete.
The unique-target count of 557 agrees with both the audit and the retired
string-level scan.

## 7. Duplicate labels

Zero duplicates at LaTeX semantics, before and after: 1201 label definitions and
1201 distinct keys after the repair, 1197 and 1197 before. The heading-generated
family and the explicit `\label` family do not collide with each other.

## 8. JSON parse results and digest binding

Every control JSON parses, including the two edited by this pass and the one
carrying the audit-trail note:

```
claim-ledger.json          PARSE_OK  top-level keys 6
adversarial-report.json    PARSE_OK  top-level keys 8
approach-registry.json     PARSE_OK  top-level keys 8
problem-contract.json      PARSE_OK  top-level keys 4
dependency-dag.json        PARSE_OK  top-level keys 5

artifact bindings checked 37   mismatches 0   null(not-run) 1
claim-ledger: 67 claims  {'CANDIDATE': 25, 'EVIDENCE_VERIFIED': 42}
unique evidence artifact paths: 19
adversarial-report.oracle_erasure.result = NOT_RUN
attack dispositions: ['REJECTED', 'REJECTED_AFTER_REPAIR']
```

Every `artifact_path` and `artifact_sha256` pair in the run package now
recomputes against current bytes with **zero mismatches**. The single null pair
is `oracle_erasure`, which remains `NOT_RUN`.

**What was changed in the JSON, and what was not.**

* `claim-ledger.json`: the stale `evidence/task-9-integrated-proof.md` digest was
  replaced at its **2** occurrences. The replacement is a same-length 64-character
  substitution, so the file length is unchanged at 83,546 bytes. No claim, no
  state, no scope, and no other digest was touched. The state census is
  unchanged: 42 `EVIDENCE_VERIFIED`, 25 `CANDIDATE`, 0 `REFUTED`, 0
  `INCONCLUSIVE`, and all twelve Task 10 claims remain `CANDIDATE`.
* `adversarial-report.json`: the same digest was replaced at its **3**
  occurrences, again same-length, file length unchanged at 21,532 bytes. No
  attack, response, or disposition was altered, and `oracle_erasure` remains
  `NOT_RUN`.
* `approach-registry.json`: one entry was appended to the `reconciliation` array,
  which is the array of `{issue, resolution}` process records and carries no
  digests and no mathematical dispositions. It records the FAIL audit, the
  four-line repair, and the retirement of the string-level check, and names this
  artifact by path. A structural comparison confirms that every other top-level
  key and all nine pre-existing reconciliation entries are unchanged; the array
  went from 9 entries to 10.
* No new evidence binding was added anywhere, which is what keeps the hash
  dependency acyclic.

## 9. `git diff --check`

```
$ git diff --check
warning: in the working copy of 'docs/.../adversarial-report.json', LF will be replaced by CRLF ...
warning: in the working copy of 'docs/.../approach-registry.json', LF will be replaced by CRLF ...
warning: in the working copy of 'docs/.../claim-ledger.json', LF will be replaced by CRLF ...
warning: in the working copy of 'docs/.../counterexample-register.md', LF will be replaced by CRLF ...
exit=0
```

Exit code `0`, zero whitespace errors. The four messages are `core.autocrlf`
advisories about pre-existing LF files, not `--check` findings, and they are the
same four the audit recorded before this pass. A direct scan of the repaired TeX
file confirms zero trailing whitespace, zero tabs, zero non-ASCII characters, and
a non-blank final line.

## 10. Bibliography

```
BIBKEYS 464   EXACT_DUPS 0   CASEINSENS_DUPS 0
CITE_SITES 99   CITED_UNIQUE 79   UNDEFINED 0
   JonaLasinio2001    defined=True cited=True
   KemenySnell1976    defined=True cited=True
   Nakajima1958       defined=True cited=True
   Zwanzig1960        defined=True cited=True
   Arnold1998         defined=True cited=True
```

464 entries, zero duplicate keys exact and case-insensitive, 79 unique cited
keys, zero undefined. This reproduces the audit's SC-6 result. `references.bib`
was not modified by this pass and retains digest
`f520c0a7a20e994786e5946f2b6484120d371d8b90a79f37895e22666e93bded`.

## 11. Touched-file scope and protected files

`git status --short` after the pass lists the same ten modified paths as before
it, plus the untracked evidence artifacts:

```
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
 ?? docs/.../evidence/task-9-cocycle-beta-analysis.md
 ?? docs/.../evidence/task-9-hermite-analysis.md
 ?? docs/.../evidence/task-9-integrated-proof.md
 ?? docs/.../evidence/task-9-opus-adversarial.md
 ?? docs/.../evidence/task-9-primary-source-map.md
 ?? docs/.../evidence/task-9-score-dqm-analysis.md
 ?? docs/.../evidence/task-9-static-proof-control.md
```

`git diff --numstat` isolates what this pass did. Only four numbers moved:

| Path | Before | After | Attributable to |
| --- | --- | --- | --- |
| `07b_agent_network_rg.tex` | `1062 25` | `1066 33` | the four line joins |
| `approach-registry.json` | `68 13` | `69 13` | the one audit-trail entry |
| `adversarial-report.json` | `15 10` | `15 10` | same-length digest substitution |
| `claim-ledger.json` | `14 9` | `14 9` | same-length digest substitution |
| all six other paths | unchanged | unchanged | untouched by this pass |

**Files this pass was permitted to edit and did edit:**
`07b_agent_network_rg.tex`, `evidence/task-9-integrated-proof.md`,
`evidence/task-9-heading-repair.md` (this file), `claim-ledger.json`,
`adversarial-report.json`, `approach-registry.json`.

**Protected and confirmed untouched.** The three `.verification/*.json` files
remain untracked and byte-identical to their pre-pass digests, and
`manuscripts/gauge_vfe_rg/verification/current-results.json` does not appear in
`git status` at all and retains digest
`71e58869e3fb7f0f04c506f74542eb3603fa156781e82755162f2f5a1a7ce893`. The two
independent audit reports, `counterexample-register.md`, the other evidence
artifacts, the plan, the remaining manuscripts, and `references.bib` are
unmodified, each confirmed by digest in section 1 or by absence from the diff.

The verification-skill control plane remains drifted and this pass did not
silence it: no file under `.verification/` was created, deleted, moved,
re-pinned, or edited, and no `artifact_revision` was recomputed. That obligation
belongs to the verification skill, as
`evidence/task-9-integrated-proof.md` already records.

**Validator transcript, now obtained.** `evidence/task-9-integrated-proof.md`
records as a limitation that the validator could not be executed in the
integration environment because Python invocation was gated there, so the Stop
hook's verbatim message stood in for a transcript. Python is available here, and
the documented read-only command was run:

```
$ python "C:/Users/chris and christine/.claude/skills/verification/scripts/verification_gate.py" \
    validate .verification/task3-factorization-closure-ledger.json --cwd .
live artifact changed after verification activation
exit=1
```

The validator reproduces the hook message exactly, which establishes that the
Stop hook is that validator's fail-closed check rather than an independent
condition. The activation marker pins the ledger to
`git:bcc80a032ea761669bdcb244ed51f5d8380b6c05:sha256:bf6b86ab...27de7`, and that
revision spec binds the Git index together with tracked and non-ignored untracked
worktree content while **excluding** `.git` and `.verification`. Two consequences
follow, both mechanical. First, the drift cannot be caused by anything in
`.verification/`, since that path is outside the digest; it is caused by repository
content changing. Second, the pin was already stale before this pass: six commits
landed after the pinned revision, `98bc0d8` through the current
`HEAD = 3dbe4c6`. The four-line repair adds further drift, as any edit
necessarily would.

Clearing the alarm requires either re-pinning `active.json` to a current
`artifact_revision` or committing the worktree. The first is outside this pass's
ownership and is exactly what the audit's finding N-6 says must not be done; the
second is a Git mutation the charter prohibits. The alarm is therefore left
standing and reported, which is the sanctioned outcome. The consequence is
confined to that ledger: at this worktree state the Task 3 factorization-closure
ledger may close nothing, its claims are `INCONCLUSIVE`, and the open obligation
is to re-verify at a current artifact revision. It neither certifies nor
decertifies the rigorous-theory-search closures recorded here, whose separate
binding discipline is checked in section 8 and holds.

## 12. Findings not repaired by this pass

No check beyond B-1 failed, so nothing is recorded here as a blocker. For
completeness, the following remain open exactly as the independent audit left
them, and are outside the scope of a B-1 repair:

* **N-1 through N-6**, the audit's non-blocking findings, are untouched. N-3
  (two abbreviated bibliography titles) and N-4 (`task-9-primary-source-map.md`
  is present in `evidence/` but bound by no control record) would require editing
  `references.bib` or adding an evidence binding, both outside this scope. N-5
  concerns one characterization inside the integrated proof's status-tag bullet;
  the audit assigns that repair to the Task 11 status sweep, and this pass left
  the bullet as written while flagging it in the integrated proof's section 7.1.
* **No TeX build was run**, as the charter requires. B-1 therefore rests on the
  macro arity quoted in section 2 and on standard TeX undelimited-argument
  scanning, which is the same basis the audit used. The falsification condition
  is unchanged: a `pdflatex` run over `main.tex` at the pre-repair bytes that
  nonetheless defined all four labels and resolved all six references would
  refute it.
* **The Task 3 verification-skill ledger drift** is real, predates this pass, and
  is reported rather than silenced.

## 13. Conclusion

**PASS.**

1. B-1 is repaired at all four sites in `07b_agent_network_rg.tex`, by exactly the
   minimal repair the audit prescribed, and byte-level reconstruction proves
   nothing else in the file changed.
2. A check that detects the defect class, a heading-arity-aware scanner requiring
   both mandatory arguments to be brace groups, was run over the repaired bytes
   and reports zero malformed calls, zero duplicate labels, and zero unresolved
   reference targets. The same check reports FAIL on the pre-repair bytes, so it
   is demonstrated to have the discriminating power the retired string-level scan
   lacked.
3. The source digest in `evidence/task-9-integrated-proof.md` section 3 and the
   evidence digests in `claim-ledger.json` and `adversarial-report.json` were
   recomputed against the new bytes; all 37 artifact bindings in the run package
   verify with zero mismatches.

These are the three conditions section 5 of `evidence/task-9-opus-adversarial.md`
names for converting its FAIL to PASS. The audit records no mathematical
blocker, and no mathematical content was changed by this pass.
