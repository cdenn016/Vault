"""Map 'Underfull \\vbox ... while \\output is active' warnings to the page shipped out next."""
import re, sys
BS = chr(92)
for fn in sys.argv[1:]:
    t = open(fn, encoding='latin-1').read()
    ev = [(m.start(), 'U') for m in re.finditer('Underfull ' + re.escape(BS) + 'vbox', t)]
    ev += [(m.start(), m.group(1)) for m in re.finditer(r'\[(\d+)(?=[\s\]{])', t)]
    ev.sort()
    pend, out = False, []
    for pos, e in ev:
        if e == 'U':
            pend = True
        elif pend:
            out.append(int(e))
            pend = False
    print(fn.split('/')[-1], '-> underfull vbox on pages', out)
