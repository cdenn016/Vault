"""Audit display-equation terminal punctuation against the following text."""
import re
BS = chr(92)
base = r"C:/Users/chris and christine/Desktop/Research/manuscripts/"
docs = {'main': 'GL(K)_attention_v2.tex', 'supp': 'GL(K)_supplementary_v2.tex'}
env_re = re.compile(re.escape(BS) + r'begin\{(equation|align|gather|multline)(\*?)\}(.*?)' + re.escape(BS) + r'end\{\1\2\}', re.S)
for d, f in docs.items():
    src = open(base + f, encoding='utf-8').read()
    starts = [0] + [m.end() for m in re.finditer('\n', src)]
    import bisect
    ln = lambda off: bisect.bisect_right(starts, off)
    for m in env_re.finditer(src):
        body = m.group(3)
        # strip labels, nonumber, comments
        b = re.sub(re.escape(BS) + r'label\{[^}]*\}', '', body)
        b = re.sub(re.escape(BS) + r'nonumber', '', b)
        b = re.sub(r'%.*', '', b)
        b = b.rstrip()
        # strip trailing \end{cases} / \end{aligned} / \right) etc to find last visible char
        tail = b[-40:].replace('\n', ' ')
        last = b.rstrip()[-1:] if b else ''
        # what the display's last row ends with: ',' '.' or other
        endpunct = last if last in ',.;' else 'NONE'
        # find inner rows ending (align rows separated by \\)
        rows = re.split(re.escape(BS + BS), b)
        row_ends = []
        for r in rows[:-1]:
            r2 = re.sub(re.escape(BS) + r'(qquad|quad)', '', r).rstrip()
            row_ends.append(r2[-1:] if r2 else '')
        after = src[m.end():m.end() + 200]
        blank_after = bool(re.match(r'[ \t]*\n[ \t]*\n', after))
        before = src[max(0, m.start() - 60):m.start()]
        blank_before = bool(re.search(r'\n[ \t]*\n[ \t]*$', before))
        nxt = re.sub(r'^\s+', '', after)
        nxt_word = nxt.split()[0] if nxt.split() else ''
        cont = nxt_word[:1].islower() or nxt_word.startswith(BS + 'begin') is False and nxt_word[:1] in '('
        flag = []
        if endpunct == 'NONE' and nxt_word[:1].isupper():
            flag.append('MISSING-PERIOD?')
        if endpunct == '.' and nxt_word[:1].islower():
            flag.append('PERIOD-BEFORE-LOWERCASE')
        if endpunct == ',' and nxt_word[:1].isupper() and not nxt_word.startswith(BS):
            flag.append('COMMA-BEFORE-UPPERCASE')
        if blank_before:
            flag.append('BLANK-LINE-BEFORE')
        if blank_after and nxt_word[:1].islower():
            flag.append('BLANK-LINE-THEN-LOWERCASE(new indented paragraph)')
        print(f"{d}:{ln(m.start())}-{ln(m.end())} env={m.group(1)} end={endpunct!r:6} rows={row_ends} next={nxt_word[:25]!r} {' '.join(flag)}")
