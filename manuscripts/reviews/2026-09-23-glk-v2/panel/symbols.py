"""Extract math-mode symbol atoms (base glyph + font + first sub/superscript) with line numbers."""
import re, collections, sys
BS = chr(92)
base = r"C:/Users/chris and christine/Desktop/Research/manuscripts/"
docs = {'main': 'GL(K)_attention_v2.tex', 'supp': 'GL(K)_supplementary_v2.tex'}

def math_segments(src):
    """Yield (start_offset, text) of math segments."""
    segs = []
    envs = ['equation', 'equation*', 'align', 'align*', 'gather', 'multline', 'aligned']
    # display environments
    for env in ['equation', 'align', 'gather', 'multline']:
        for m in re.finditer(re.escape(BS + 'begin{' + env) + r'\*?\}(.*?)' + re.escape(BS + 'end{' + env) + r'\*?\}', src, re.S):
            segs.append((m.start(1), m.group(1)))
    for m in re.finditer(re.escape(BS + '[') + r'(.*?)' + re.escape(BS + ']'), src, re.S):
        segs.append((m.start(1), m.group(1)))
    for m in re.finditer(re.escape(BS + '(') + r'(.*?)' + re.escape(BS + ')'), src, re.S):
        segs.append((m.start(1), m.group(1)))
    # inline $...$ (not $$)
    for m in re.finditer(r'(?<![\\$])\$([^$]+?)\$', src, re.S):
        segs.append((m.start(1), m.group(1)))
    return segs

greek = ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'varepsilon', 'zeta', 'eta', 'theta', 'vartheta', 'iota', 'kappa', 'lambda', 'mu', 'nu', 'xi', 'pi', 'varpi', 'rho', 'varrho', 'sigma', 'varsigma', 'tau', 'upsilon', 'phi', 'varphi', 'chi', 'psi', 'omega', 'Gamma', 'Delta', 'Theta', 'Lambda', 'Xi', 'Pi', 'Sigma', 'Upsilon', 'Phi', 'Psi', 'Omega', 'ell', 'partial', 'nabla']
fonts = ['mathcal', 'mathsf', 'mathbb', 'mathfrak', 'mathbf', 'boldsymbol', 'mathrm', 'mathbbm', 'widetilde', 'tilde', 'bar', 'overline', 'hat', 'widehat', 'mathsf']
tok_re = re.compile(
    r'(?P<font>' + re.escape(BS) + r'(?:' + '|'.join(fonts) + r')\s*\{\s*(?:' + re.escape(BS) + r'[A-Za-z]+|[A-Za-z0-9])\s*\}|' + re.escape(BS) + r'(?:' + '|'.join(fonts) + r')\s+[A-Za-z])'
    r'|(?P<greek>' + re.escape(BS) + r'(?:' + '|'.join(greek) + r'))(?![A-Za-z])'
    r'|(?P<latin>(?<![A-Za-z\\])[A-Za-z](?![A-Za-z]))'
)
script_re = re.compile(r'\s*([_^])\s*(\{(?:[^{}]|\{[^{}]*\})*\}|' + re.escape(BS) + r'[A-Za-z]+|.)')

out = collections.defaultdict(lambda: collections.defaultdict(list))
for d, f in docs.items():
    src = open(base + f, encoding='utf-8').read()
    # blank out tikz pictures? keep, they carry labels shown to reader
    line_starts = [0]
    for m in re.finditer('\n', src):
        line_starts.append(m.end())
    import bisect
    def lineno(off):
        return bisect.bisect_right(line_starts, off)
    # remove text commands content inside math
    for start, seg in math_segments(src):
        clean = re.sub(re.escape(BS) + r'(text|mathrm|operatorname|label|eqref|ref|texttt|mbox)\s*\{[^{}]*\}', lambda m: ' ' * len(m.group(0)), seg)
        clean = re.sub(re.escape(BS) + r'(begin|end)\{[a-z*]+\}', lambda m: ' ' * len(m.group(0)), clean)
        for m in tok_re.finditer(clean):
            g = m.group(0)
            if m.group('latin') and g in 'd':
                pass
            pos = m.end()
            scripts = ''
            for _ in range(2):
                sm = script_re.match(clean, pos)
                if not sm:
                    break
                scripts += sm.group(1) + sm.group(2)
                pos = sm.end()
            key = re.sub(r'\s+', '', g)
            out[key][re.sub(r'\s+', '', scripts)].append((d, lineno(start + m.start())))

for key in sorted(out, key=lambda k: k.lower()):
    variants = out[key]
    total = sum(len(v) for v in variants.values())
    print(f"## {key}  (total {total})")
    for sc, occ in sorted(variants.items(), key=lambda kv: (kv[1][0][0] != 'main', kv[1][0][1])):
        first = occ[0]
        lines = sorted(set(f"{x[0][0]}{x[1]}" for x in occ), key=lambda s: (s[0], int(s[1:])))
        print(f"   {key}{sc:30s} first={first[0]}:{first[1]}  n={len(occ)}  lines={' '.join(lines[:14])}{' ...' if len(lines) > 14 else ''}")
