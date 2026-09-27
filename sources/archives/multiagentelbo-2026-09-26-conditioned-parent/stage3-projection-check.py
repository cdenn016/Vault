"""Exact projection checks for the inherited scalar-cycle parent; no simulation."""
from fractions import Fraction as F
from pathlib import Path
import json

def dot(x: list[F], y: list[F]) -> F:
    return sum((a*b for a,b in zip(x,y)), F(0))

def add(x: list[F], y: list[F], scale: F=F(1)) -> list[F]:
    return [a+scale*b for a,b in zip(x,y)]

def outer(x: list[F], y: list[F]) -> list[list[F]]:
    return [[a*b for b in y] for a in x]

def mv(A: list[list[F]], x: list[F]) -> list[F]:
    return [dot(row,x) for row in A]

def mm(A: list[list[F]], B: list[list[F]]) -> list[list[F]]:
    return [[dot(row,list(col)) for col in zip(*B)] for row in A]

def residual(edge: int, channel: int) -> list[F]:
    a=[F(0)]*12
    a[channel+edge]=-1
    a[channel+(edge+1)%4]=1
    a[8+edge]=-1
    return a

I=[[F(i==j) for j in range(12)] for i in range(12)]
D=[[F(j==i)-F(j==4+i) for j in range(12)] for i in range(4)]
Omega=[[I[i][j]+2*sum(v[i]*v[j] for v in D) for j in range(12)] for i in range(12)]
records=[]
for edges in [(0,2),(1,3)]:
    ab=[residual(e,0) for e in edges]
    am=[residual(e,4) for e in edges]
    plus=[add(b,m) for b,m in zip(ab,am)]
    Z=[add(plus[0],plus[1],F(-1)),add(ab[0],am[0],F(-1)),add(ab[1],am[1],F(-1))]
    H=[[2*sum(v[i]*v[j] for v in ab+am) for j in range(12)] for i in range(12)]
    P=[[I[i][j]-sum(v[i]*v[j]/dot(v,v) for v in Z) for j in range(12)] for i in range(12)]
    assert [[dot(v,w) for w in Z] for v in Z]==[[F(16),0,0],[0,F(4),0],[0,0,F(4)]]
    for v,h,o in zip(Z,[8,4,4],[1,5,5]):
        assert mv(H,v)==[h*x for x in v]
        assert mv(Omega,v)==[o*x for x in v]
    assert mm(P,P)==P and mm(P,H)==mm(H,P) and mm(P,Omega)==mm(Omega,P)
    assert sum(P[i][i] for i in range(12))==9
    loop=[F(0)]*8+[F(1)]*4
    common=add(plus[0],plus[1])
    assert mv(P,loop)==loop and mv(P,common)==common
    records.append(dict(edges=edges,hidden_dimension=3,retained_dimension=9,hidden_H_eigenvalues=[8,4,4],hidden_Omega_eigenvalues=[1,5,5],projector_idempotent=True,drift_reducing=True,loop_retained=True,common_fast_normal_retained=True))
out=dict(arithmetic='Python Fraction exact',matching_checks=records,scope='Algebra of the fixed channel only; not a substitute for the conditional or path proofs.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
