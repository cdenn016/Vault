import os
os.environ["OMP_NUM_THREADS"]="2"; os.environ["OPENBLAS_NUM_THREADS"]="2"; os.environ["MKL_NUM_THREADS"]="2"
import numpy as np, time
rng=np.random.default_rng(7)
t0=time.time()

def spd(K,cond):
    Q,_=np.linalg.qr(rng.standard_normal((K,K)))
    ev=np.exp(rng.uniform(-cond,cond,K))
    return Q@np.diag(ev)@Q.T

def model(N,K,edges,law,cscale=1.0,sanc=None):
    # edges: list of (i,j) receiver i, sender j. returns Jacobian of per-agent mean flow and content gain blocks
    P=[spd(K,2.5) for _ in range(N)]            # self precisions
    T={e:rng.standard_normal((rng.integers(1,K+1),K)) for e in edges}
    R={e:(lambda M:M@M.T+1e-3*np.eye(M.shape[0]))(rng.standard_normal((T[e].shape[0],T[e].shape[0]))*np.exp(rng.uniform(-3,1))) for e in edges}
    c=[cscale*rng.standard_normal(K) for _ in range(N)]
    s=np.exp(rng.uniform(-2,2)) if sanc is None else sanc
    ins={i:[e for e in edges if e[0]==i] for i in range(N)}
    Sig=[np.linalg.inv(P[i]) for i in range(N)]   # start
    def build(Sig):
        A=[];Ls={}
        Nt={}
        for i in range(N):
            d=K+K*K*len(ins[i]); Ai=np.zeros((d,d)); Ai[:K,:K]=P[i]
            kap=np.kron(np.eye(K),c[i][None,:])
            for k,e in enumerate(ins[i]):
                sl=slice(K+k*K*K,K+(k+1)*K*K); Ai[sl,sl]+=s*np.eye(K*K)
                L=np.zeros((T[e].shape[0],d)); L[:,:K]=T[e]; L[:,sl]=-T[e]@kap
                Ne=R[e]+(T[e]@Sig[e[1]]@T[e].T if law else 0)
                Ai+=L.T@np.linalg.solve(Ne,L); Ls[e]=L; Nt[e]=Ne
            A.append(Ai)
        return A,Ls,Nt
    if law:
        for it in range(4000):
            A,Ls,Nt=build(Sig)
            new=[np.linalg.inv(A[i])[:K,:K] for i in range(N)]
            err=max(np.abs(new[i]-Sig[i]).max() for i in range(N)); Sig=new
            if err<1e-13: break
    A,Ls,Nt=build(Sig)
    off=np.cumsum([0]+[a.shape[0] for a in A]); D=off[-1]
    J=-np.eye(D); G=np.zeros((N*K,N*K)); gains={}
    for i in range(N):
        Ainv=np.linalg.inv(A[i])
        for e in ins[i]:
            j=e[1]; blk=Ainv@Ls[e].T@np.linalg.solve(Nt[e],T[e])
            J[off[i]:off[i+1],off[j]:off[j]+K]+=blk
            G[i*K:(i+1)*K,j*K:(j+1)*K]+=blk[:K]; gains[e]=blk[:K]
    post=[np.linalg.inv(A[i])[:K,:K] for i in range(N)]
    return J,G,gains,P,T,Nt,post

# 0. MA instance of it2:open-convergence (plug-in), q=1 and q=0.25
for q in (0.25,0.5,1.0):
    P0=np.array([[10.,3],[3,1]]);P1=np.array([[1.,3],[3,10]])
    G=np.zeros((4,4)); G[:2,2:]=q*np.linalg.inv(P0+q*np.outer([1,0],[1,0]))@np.outer([1,0],[1,0])
    G[2:,:2]=q*np.linalg.inv(P1+q*np.outer([0,1],[0,1]))@np.outer([0,1],[0,1])
    ev=np.linalg.eigvals(-np.eye(4)+G); print("q",q,"max Re",ev.real.max(),"pred",-1+3*q/(1+q), "CA value a_a a_b x/(1+Rc)^2 =",0.9*10/(1+1/q)**2,"(3q/(1+q))^2 =",(3*q/(1+q))**2)

# 1. rings: spectrum identity and law-level stability, bound of C4-type
worst_law=-9; worst_plug=-9; nplug_unst=0; maxid=0; maxbound=0; nring=0
for trial in range(1500):
    N=int(rng.integers(2,5)); K=int(rng.integers(2,4))
    edges=[(i,(i+1)%N) for i in range(N)]
    st=rng.bit_generator.state
    for law in (True,False):
        rng.bit_generator.state=st
        J,G,gains,P,T,Nt,post=model(N,K,edges,law)
        ev=np.linalg.eigvals(J)
        # cycle product
        Ac=np.eye(K)
        for i in range(N): Ac=Ac@gains[(i,(i+1)%N)]  # A_{0<-1} A_{1<-2} ... 
        tau=np.linalg.eigvals(Ac)
        pred=max((t.astype(complex)**(1/N)*np.exp(2j*np.pi*k/N)).real for t in tau for k in range(N))-1
        pred=max(pred,-1.0)
        maxid=max(maxid,abs(ev.real.max()-pred))
        if law:
            worst_law=max(worst_law,ev.real.max())
            b=1.0
            for e in edges:
                i,j=e; X=T[e]@np.linalg.inv(P[i])@T[e].T
                # effective noise incl. dictionary: recover from posterior: T post_i T^T = (X^-1+Neff^-1)^-1
                Yi=T[e]@post[i]@T[e].T; Neff=np.linalg.inv(np.linalg.inv(Yi)-np.linalg.inv(X))
                snrf=np.linalg.eigvals(np.linalg.solve(X+Neff,X)).real.max()
                rp=np.linalg.eigvals(np.linalg.solve(Neff,T[e]@post[j]@T[e].T)).real.max()
                b*=np.sqrt(rp*snrf)
            rho=np.abs(tau).max(); maxbound=max(maxbound,rho/b); nring+=1
            assert rho<=b*(1+1e-7)+1e-12,(rho,b)
        else:
            worst_plug=max(worst_plug,ev.real.max()); nplug_unst+=ev.real.max()>1e-9
print("rings:",nring,"max |maxRe - pred from A_c|",maxid,"law-level worst max Re",worst_law,"max rho/bound",maxbound,"plug-in worst",worst_plug,"plug-in unstable count",nplug_unst)

# 2. general digraphs, law-level, lambda=0: search for instability
worst=-9; cnt=0; nun=0; arg=None
while time.time()-t0<40:
    N=int(rng.integers(3,5)); K=2
    edges=[(i,j) for i in range(N) for j in range(N) if i!=j and rng.random()<0.6]
    if not edges: continue
    J,G,gains,P,T,Nt,post=model(N,K,edges,True,cscale=0.0)
    m=np.linalg.eigvals(J).real.max(); cnt+=1
    if m>worst: worst=m; arg=(N,edges)
    nun+=m>1e-9
print("general digraphs law-level:",cnt,"instances, worst max Re",worst,"unstable",nun,arg)
print("time",time.time()-t0)
