import numpy as np, itertools
def omega(A,d,tbar):
    n=A.shape[0]; D=np.diag(d); P=[np.eye(n)]
    for _ in range(tbar-1): P.append(P[-1]@A)
    L=np.zeros((n*tbar,n*tbar))
    for t in range(tbar):
        for s in range(t+1): L[t*n:(t+1)*n,s*n:(s+1)*n]=P[t-s]
    S=L@np.kron(np.eye(tbar),D)@L.T; tot=0;c=0
    for i in range(n):
        ii=[t*n+i for t in range(tbar)]
        for j in range(i+1,n):
            jj=[t*n+j for t in range(tbar)]
            tot+=0.5*(np.linalg.slogdet(S[np.ix_(ii,ii)])[1]+np.linalg.slogdet(S[np.ix_(jj,jj)])[1]-np.linalg.slogdet(S[np.ix_(ii+jj,ii+jj)])[1]);c+=1
    return tot/c
A4=np.array([[0.5,0.2,0.1,0.0],[0.15,0.4,0.25,0.0],[0.0,0.1,0.5,0.3],[0.0,0.0,0.2,0.3]])
d=np.array([0.5,0.4,0.3,0.6]); l=np.array([0.7,0.5,0.9,0.4]); Q=np.diag(d)+np.outer(l,l); v=1.2*l**2; dlo=np.diag(Q)-v
print("dlo",dlo,"diagQ",np.diag(Q))
def bound(A):
    n=4;terms=[]
    for i in range(n):
        for j in range(i+1,n):
            def r2(a,b):
                num=A[a,b]**2*dlo[b]; den=num+sum(A[a,m]**2*Q[m,m] for m in range(n) if m!=b)+Q[a,a]; return num/den
            terms.append(-0.5*np.log(1-max(r2(i,j),r2(j,i))))
    return np.mean(terms)
def report(A,name):
    rng=np.random.default_rng(0)
    corners=[omega(A,np.where(np.array(b),np.diag(Q),dlo),2) for b in itertools.product([0,1],repeat=4)]
    pts=rng.uniform(dlo,np.diag(Q),(2000,4)); vals=[omega(A,p,2) for p in pts]
    feas=np.array([np.linalg.eigvalsh(Q-np.diag(p)).min()>=0 for p in pts])
    allv=corners+vals
    fv=np.array(vals)[feas]
    print(name,"t4 idD %.4f Qii %.4f | bound %.6f | box [%.4f,%.4f] | feas frac %.4f"%(omega(A,d,4),omega(A,np.diag(Q),4),bound(A),min(allv),max(allv),feas.mean()),
          "feas range", (fv.min(),fv.max()) if feas.any() else None, "k1 val t2 %.6f"%omega(A,d,2))
report(A4,"A4 (record)")
offs=[(i,j) for i in range(4) for j in range(4) if i!=j and A4[i,j]!=0]
for (i,j) in offs:
    B=A4.copy();B[i,j]=0;report(B,"drop%d%d"%(i,j))
print("corner feasibility:",[ (b, round(np.linalg.eigvalsh(Q-np.diag(np.where(np.array(b),np.diag(Q),dlo))).min(),4)) for b in itertools.product([0,1],repeat=4)])
