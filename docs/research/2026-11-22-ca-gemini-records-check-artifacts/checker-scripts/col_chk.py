import os
for v in ("OMP_NUM_THREADS","MKL_NUM_THREADS","OPENBLAS_NUM_THREADS"): os.environ[v]="2"
import math, itertools, numpy as np
from scipy import sparse, linalg
from scipy.sparse.linalg import eigsh
P=math.pi/math.sqrt(12)
def lap2d(sites):
    idx={s:k for k,s in enumerate(sites)}; n=len(sites); r=[];c=[];v=[]; deg=np.zeros(n)
    for k,(x,y) in enumerate(sites):
        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
            j=idx.get((x+dx,y+dy))
            if j is not None: r.append(k);c.append(j);v.append(-1.0);deg[k]+=1
    L=sparse.csc_matrix((v,(r,c)),shape=(n,n))+sparse.diags(deg)
    return L
# (A) exact C_sigma family of the proof, direct 2D eigensolve
for sig in (16.0,64.0,256.0,600.0):
    H0=int(math.floor(sig**0.5)); M=int(math.floor(sig**0.25))
    H=[];x=0
    while True:
        h=int(math.floor((H0+0.5)*math.exp(-x*x/(2*sig*sig))))
        if h<M: break
        H.append(h); x+=1
    R=len(H)-1
    sites=[(ix,iy) for ix in range(-R,R+1) for iy in range(H[abs(ix)])]
    L=lap2d(sites); n=len(sites)
    ev=np.sort(eigsh(L,k=3,sigma=-1e-7,which="LM",return_eigenvectors=False))
    xs=np.array([s[0] for s in sites],float); var=xs.var()
    print(f"spindle sig={sig:6.0f} H0={H0} M={M} R={R} n={n} lam2*sig^2={ev[1]*sig*sig:.5f} var/sig^2={var/sig/sig:.5f} Q={math.sqrt(var*ev[1]):.5f} (pi/sqrt12={P:.5f})")
# (B) row 5 kernel: exhaustive subsets of 4x4 window containing corner; r, r_star
a1,a2,ad,eps=6/70,9/280,9/140,18/35
offs=[((1,0),a1),((-1,0),a1),((0,1),a1),((0,-1),a1),((2,0),a2),((-2,0),a2),((0,2),a2),((0,-2),a2),((1,1),ad),((1,-1),ad),((-1,1),ad),((-1,-1),ad)]
cells=[(i,j) for i in range(4) for j in range(4)]
best_r=best_s=0
for mask in range(1,1<<16):
    if not mask&1: continue
    S=[cells[k] for k in range(16) if mask>>k&1]; n=len(S)
    if n<2: continue
    ix={s:k for k,s in enumerate(S)}; L=np.zeros((n,n)); cut=0.0
    for k,(x,y) in enumerate(S):
        for (dx,dy),w in offs:
            j=ix.get((x+dx,y+dy))
            if j is None: cut+=w
            else: L[k,j]-=w; L[k,k]+=w
    l2=np.linalg.eigvalsh(L)[1]
    r=(eps+l2)/(eps+cut/n); s=l2/(cut/n)
    if r>best_r: best_r=r;Sr=S
    if s>best_s: best_s=s;Ss=S
print("row5 4x4 window: max r=%.4f (n=%d) max r*=%.4f (n=%d)"%(best_r,len(Sr),best_s,len(Ss)), Ss)
# (C) random connected regions in Z^3 nn: r_star<1 ; Z^2 nn r_star<=1
rng=np.random.default_rng(1)
for D in (2,3,4):
    mx=0
    for t in range(4000):
        n=int(rng.integers(2,30)); S={tuple([0]*D)}
        while len(S)<n:
            p=list(S)[rng.integers(len(S))]; d=rng.integers(D); q=list(p); q[d]+=rng.choice([-1,1]); S.add(tuple(q))
        S=list(S); ix={s:k for k,s in enumerate(S)}; L=np.zeros((n,n)); cut=0
        for k,p in enumerate(S):
            for d in range(D):
                for sg in (-1,1):
                    q=list(p);q[d]+=sg;j=ix.get(tuple(q))
                    if j is None: cut+=1
                    else: L[k,j]-=1;L[k,k]+=1
        mx=max(mx,np.linalg.eigvalsh(L)[1]/(cut/n))
    # boxes of side 2
    print(f"Z^{D} nn random Eden regions n<30: max r* = {mx:.4f}; 2^D cube r*={2/(2*D-D):.4f}")
# (D) horn graph reduction test (small): cliques weight K, matchings weight 1
for (al,M,R,K) in ((0.3,4,6,1.0),(0.2,6,8,0.5)):
    w=[int(math.floor(M*math.exp(al*(R-abs(k))))) for k in range(-R,R+1)]
    off=np.concatenate([[0],np.cumsum(w)]); N=off[-1]; A=np.zeros((N,N))
    for li in range(2*R+1):
        A[off[li]:off[li+1],off[li]:off[li+1]]=K
    np.fill_diagonal(A,0)
    for li in range(2*R):
        m=min(w[li],w[li+1])
        for y in range(m): A[off[li]+y,off[li+1]+y]=A[off[li+1]+y,off[li]+y]=1
    L=np.diag(A.sum(1))-A; l2=np.linalg.eigvalsh(L)[1]
    e=np.array([min(w[i],w[i+1]) for i in range(2*R)],float); W=np.array(w,float)
    T=np.zeros((2*R+1,2*R+1))
    for i in range(2*R): T[i,i]+=e[i];T[i+1,i+1]+=e[i];T[i,i+1]-=e[i];T[i+1,i]-=e[i]
    l1d=linalg.eigh(T,np.diag(W),eigvals_only=True)[1]
    xs=np.concatenate([[k]*w[k+R] for k in range(-R,R+1)]).astype(float)
    s2=max((A*(xs[:,None]-xs[None,:])**2).sum(1))
    print(f"horn al={al} M={M} R={R} K={K} N={N}: varsigma2={s2}, lam2(graph)={l2:.6f}, lam1D={l1d:.6f}, lam1D/(1+4/(K*M))={l1d/(1+4/(K*M)):.6f}, Barta (1-e^-al/2)^2={(1-math.exp(-al/2))**2:.6f}, diam*sqrt(lam2)/ln N={2*R*math.sqrt(l2)/math.log(N):.4f}")
