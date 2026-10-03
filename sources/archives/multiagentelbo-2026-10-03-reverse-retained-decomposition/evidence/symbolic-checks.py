"""Exact finite algebra grounding for the provisional reverse decomposition."""
from pathlib import Path
import json
import time
import sympy as s


def main() -> None:
    """Check correlated projection, entropy algebra, and a Gaussian calibration."""
    started=time.perf_counter()
    P=s.Matrix([[1,1,0]])
    Q=s.Matrix([[3,1,0],[1,2,s.Rational(1,2)],[0,s.Rational(1,2),2]])
    Z=s.Matrix([[1/s.sqrt(2),0],[-1/s.sqrt(2),0],[0,1]])
    Qr=P*Q*P.T; L=Q*P.T*Qr.inv(); N=s.eye(3)-L*P; W=Z.T*N; Qh=W*Q*W.T
    residuals={
        'PL_identity':P*L-s.eye(1),'PZ_zero':P*Z,'WL_zero':W*L,
        'WZ_identity':W*Z-s.eye(2),'coordinate_inverse':L*P+Z*W-s.eye(3),
        'independent_noise':W*Q*P.T,'noise_reconstruction':L*Qr*L.T+Z*Qh*Z.T-Q,
    }
    F=s.Matrix(3,3,s.symbols('f0:9',real=True));f=s.Matrix(s.symbols('f9:12',real=True))
    x=s.Matrix(s.symbols('x0:3',real=True));u=s.Matrix([s.symbols('u',real=True)])
    vhat=N*(F*x+f)+L*u
    residuals['retained_drift']=P*vhat-u
    residuals['hidden_drift']=W*vhat-W*(F*x+f)
    for name,value in residuals.items():
        value=value.applyfunc(s.simplify);assert value==s.zeros(*value.shape),name
    qminors=[s.det(Q[:n,:n]) for n in range(1,4)]
    hminors=[s.det(Qh[:n,:n]) for n in range(1,3)]
    assert all(value>0 for value in qminors+hminors)

    c=s.Rational(4,5);weights=[s.Rational(1,2)]*2
    probs=[s.Rational(9,10),s.Rational(1,10)]
    geom=s.sqrt(probs[0]*probs[1]);normalizer=2*geom
    full=sum(w*(c*s.log(c/p)+(1-c)*s.log((1-c)/(1-p))) for w,p in zip(weights,probs))
    separated=c*s.log(2*c)+(1-c)*s.log(2*(1-c))-s.log(normalizer)
    assert s.expand_log(s.simplify(full-separated),force=True).simplify()==0
    psi=lambda a,b:a*s.log(a/b)-a+b
    visible=sum(w*psi(1-c,1-p) for w,p in zip(weights,probs))
    separated_visible=psi(1-c,geom)+s.Rational(1,2)-geom
    assert s.expand_log(s.simplify(visible-separated_visible),force=True).simplify()==0

    # Native drift matrix [[-1,1/2],[1/2,-1]] has positive sheet precision.
    # The exact Kalman covariance is stationary at S0=2*(sqrt(5)-2).
    t=s.symbols('t',nonnegative=True);b=s.Integer(1);k=s.Rational(1,2)
    S0=2*(s.sqrt(5)-2)
    assert s.simplify(1-2*b*S0-k*k*S0*S0)==0
    V=s.Rational(1,2)+(S0-s.Rational(1,2))*s.exp(-2*t)
    M=S0*S0*k*k/s.Integer(2)*(1-s.exp(-2*t))
    checks={
        'conditional_covariance_ode':s.diff(V,t)-(1-2*b*V),
        'mean_difference_variance_ode':s.diff(M,t)-(-2*b*M+S0*S0*k*k),
        'conditional_covariance_initial':V.subs(t,0)-S0,
        'mean_difference_initial':M.subs(t,0),
    }
    for key,value in checks.items():assert s.simplify(value)==0,key
    auxiliary=s.integrate(k*k*(V+M)/2,(t,0,1))
    residual_mean=s.integrate(k*k*M/2,(t,0,1))
    output={
        'status':'algebra_checks_pass','sympy':s.__version__,
        'scope':'Finite algebra grounding only; not a general stochastic proof or O1 closure.',
        'matrix_residuals':{key:[[str(s.simplify(v)) for v in value.row(i)] for i in range(value.rows)] for key,value in residuals.items()},
        'noise_spd_leading_minors':list(map(str,qminors)),
        'hidden_noise_spd_leading_minors':list(map(str,hminors)),
        'full_source_identity_residual':'0','visible_source_identity_residual':'0',
        'example_full_source_cost':float(full),'example_geometric_normalization_cost':float(-s.log(normalizer)),
        'example_visible_source_cost':float(visible),
        'calibration':{'sheet_precision_eigenvalues':['1/2','3/2'],'stationary_filter_covariance':str(S0),
                       'ode_residuals':{key:str(s.simplify(value)) for key,value in checks.items()},
                       'one_unit_auxiliary_drift_cost':float(auxiliary),
                       'one_unit_mean_remainder_after_trace_removal':float(residual_mean),
                       'retained_relative_entropy':'0 under the exact linear Gaussian parent derivation',
                       'limits':'Gaussian constant-mark calibration only, outside informative-source O1 class; no saved-network accuracy conclusion.'},
        'elapsed_seconds':time.perf_counter()-started,
    }
    target=Path(__file__).with_name('symbolic-checks.json');target.write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8');print(json.dumps(output,indent=2))


if __name__=='__main__':main()
