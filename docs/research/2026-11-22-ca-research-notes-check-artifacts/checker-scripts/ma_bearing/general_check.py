import os
os.environ["OMP_NUM_THREADS"]="2"; os.environ["OPENBLAS_NUM_THREADS"]="2"; os.environ["MKL_NUM_THREADS"]="2"
import numpy as np, time
rng=np.random.default_rng(11)
t0=time.time()
def spd(K,cond):
    Q,_=np.linalg.qr(rng.standard_normal((K,K))); ev=np.exp(rng.uniform(-cond,cond,K)); return Q@np.diag(ev)@Q.T
def draw(N,K,edges):
    P=[spd(K,2.5) for _ in range(N)]
    T={e:rng.standard_normal((rng.integers(1,K+1),K)) for e in edges}
    R={}
    for e in edges:
        r=T[e].shape[0]; M=rng.standard_normal((r,r))*np.exp(rng.uniform(-3,1)); R[e]=M@M.T+1e-3*np.eye(r)
    return P,T,R
def solve(N,K,edges,P,T,R,iters,tol=1e-14):
    ins={i:[e for e in edges if e[0]==i] for i in range(N)}
    Sig=[np.linalg.inv(P[i]) for i in range(N)]; err=1
    for it in range(iters):
        new=[]
        for i in range(N):
            A=P[i].copy()
            for e in ins[i]:
                Ne=R[e]+T[e]@Sig[e[1]]@T[e].T; A+=T[e].T@np.linalg.solve(Ne,T[e])
            new.append(np.linalg.inv(A))
        err=max(np.abs(new[i]-Sig[i]).max()/np.abs(new[i]).max() for i in range(N)); Sig=new
        if err<tol: break
    G=np.zeros((N*K,N*K))
    for i in range(N):
        for e in ins[i]:
            j=e[1]; Ne=R[e]+T[e]@Sig[j]@T[e].T
            G[i*K:(i+1)*K,j*K:(j+1)*K]+=Sig[i]@T[e].T@np.linalg.solve(Ne,T[e])
    return np.linalg.eigvals(G-np.eye(N*K)).real.max(),err,it,Sig
found=[];cnt=0;worst=-9
while time.time()-t0<38:
    N=int(rng.integers(3,5)); K=2
    edges=[(i,j) for i in range(N) for j in range(N) if i!=j and rng.random()<0.6]
    if not edges: continue
    P,T,R=draw(N,K,edges); m,err,it,_=solve(N,K,edges,P,T,R,3000); cnt+=1; worst=max(worst,m)
    if m>1e-9: found.append((m,err,it,N,edges,P,T,R))
print("instances",cnt,"worst",worst,"unstable",len(found))
np.set_printoptions(precision=6,suppress=False,linewidth=200)
for (m,err,it,N,edges,P,T,R) in sorted(found,key=lambda z:-z[0])[:2]:
    m2,err2,it2,Sig=solve(N,2,edges,P,T,R,200000,1e-15)
    print("first pass max Re",m,"rel err",err,"iters",it,"| long pass max Re",m2,"rel err",err2,"iters",it2)
    outdeg={j:sum(1 for e in edges if e[1]==j) for j in range(N)}
    print(" N",N,"edges (receiver,sender)",edges,"out-degrees",outdeg)
    print(" cond(P)",[float(np.linalg.cond(p)) for p in P])
    for e in edges: print("  e",e,"T",T[e].tolist(),"R",R[e].tolist())
    for i in range(N): print("  P",i,P[i].tolist())
print("time",time.time()-t0)
