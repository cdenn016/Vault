# Actual prefix-conditioned parent: conditional information bounds

The existing source-retaining parent can be activated from the actual late coherence-prefix law without replacing that law by a Gaussian or resetting its hidden conditional. The discarded optimizer conditional KL is at most kappa=(eta+h_b(rho))/(1-rho); with all evaluator samples retained, the full physical conditional KL is at most kappa+T. These are static conditional-information estimates. Parent path approximation is a separate result.

## Source continuity and scope

The live Research manuscript pifb2/09_section.tex defines the exact parent by a normalized pushforward and identifies its discarded conditional KL by disintegration; it separately distinguishes coherence, persistence, and autonomy. Section 13_section.tex leaves inheritance and another formation episode distinct from pairing selection. The wiki concept Meta-agents and hierarchical emergence records the same complete-actual-law activation contract for earlier supplied hierarchies, without claiming that their source learning creates those hierarchies.

In this repository the relevant construction is prop:rg-formation-endogenous-cycle(b,c,d), not a new projection. Its proof in Theory/ca_formation_proofs.tex, the parent-channel and discarded-conditional paragraphs, already provides the matching fiber and the physical evaluator tilt. The selective-interface-actual-parent.md Sections 1-4 records the analogous actual-prefix event-information argument with private coordinates. The current scalar calculation uses the unchanged twelve-dimensional carrier. The new inputs are the entropy tracking of ca_joint_selection.tex and the native matching/coherence-prefix probability from ca_selected_coherence.tex.

This result concerns late restored equilibrium coherence. It does not identify the first formed block or a recursive episode. No base transport, selective-interface rotation, new record, Gaussian path conditioning, or physical posterior conditioned on an episode is introduced.

## Target and hypotheses

Fix a temperature 0<T<=1/100 and the actual learned four-cycle process, with deterministic native source rows p(t). Let s=t_L>=1, theta=s+1, and a=T^(1/4). Fix the matching M supplied by the selection result. Suppose throughout [s,2s] that

    KL(q_t || mu_{T,p(t)})<=eta,
    TV(q_t,nu_T^M)<=delta,

where mu_{T,p} is the full frozen-row optimizer and nu_T^M is its normalized matching-sheet Gaussian with assignment M.

Let E be the actual configuration-assignment event on [s,s+1] that the assignment is M throughout, the stacked belief/model residual norm on each matching edge is at most a, and each exterior stacked residual norm exceeds a. The current persistence theorem gives

    r:=P(E^c)<=rho:=3delta+b(T,a,1),
    b(T,a,h)=8sqrt(2/pi)a+(8+3400h)T/a^2.

Assume rho<1/2. The event E is measurable at theta. For all later t, define the actual conditional law

    q_t^E=Law(X_t,S_t | E).

The event is fixed once at activation. The future is not conditioned on subsequent coherence, remaining on M, or any other future success. The deterministic native row trajectory p(t) is the trajectory of the original coupled law; it is not recomputed from q_t^E merely because we conditioned an analysis.

The parent activates with exactly

    mu_act=C#q_theta^E.

The physical/evaluator version uses the same conditional configuration law with its actual recognition evaluator coupling, and C is extended by the identity on those samples. Both are normalized pushforwards. No product approximation is used in mu_act.

## The existing marked channel and its fibers

On a matching M with edges e,f, let F_M have the orthonormal columns

    (n_e^+-n_f^+)/sqrt(2), n_e^-, n_f^-.

Write Z_M=im(F_M), W_M=Z_M^perp, x=y+F_M z. The channel is

    C(x,S)=(S,P_{W_S}x),

with W_S=R^12 off the two matchings. Its target is the finite disjoint union of these strata. Every source assignment and the loop sum_i omega_i is retained; the matching stratum has nine continuous coordinates and the nonmatching strata retain all twelve. The map is fixed before conditioning.

The identities H_M n_g^+=8n_g^+, H_M n_g^-=4n_g^-, R_ev n_g^+=0, R_ev n_g^-=4n_g^- give the exact hidden optimizer law

    nu_{T,Z}=N(0,T K_Z^{-1}),
    K_Z=diag(8+T,4+5T,4+5T).

It is independent of y and of the prior rows. The physical outer hidden law is

    Pi_{T,Z}=N(0,T (K_Z^phys)^{-1}),
    K_Z^phys=diag(8+T,4+T,4+T).

Both inverses exist. Off matching strata the hidden conditional is a point mass and the discarded conditional KL is zero.

Define H_opt(q) to be the mean conditional KL of q given C against the optimizer's hidden conditional. On matching strata it compares the actual q(dz|S,y) with nu_{T,Z}; it does not assume that the former is Gaussian or independent of y. Define H_phys(q) by lifting q with the recognition evaluator, retaining S,y and every evaluator sample, and taking the mean discarded conditional KL against the full physical posterior at the fixed observed records.

## Conditional theorem and proof

For every t in [theta,2s],

    KL(q_t^E || mu_{T,p(t)})<=kappa,
    H_opt(q_t^E)<=kappa,
    H_phys(q_t^E)<=kappa+log[(4+5T)/(4+T)]<=kappa+T,

where

    kappa=[eta+h_b(rho)]/(1-rho),
    h_b(u)=-u log u-(1-u)log(1-u).

The same hidden-conditional bounds hold if the reference source rows at time t are replaced by any strictly positive alternative rows, including a parent's independently evolving rows. The full-law KL in the first display is claimed only for the native reference mu_{T,p(t)}.

### Event information controls the actual conditioned law

Let B=1_E and R_t=(X_t,S_t). Compute the KL of the joint law of (B,R_t) against Bernoulli(1-r) tensor mu_{T,p(t)} in two orders:

    (1-r)KL(q_t^E || mu_{T,p(t)})
       +r KL(q_t^{E^c} || mu_{T,p(t)})
     =KL(q_t || mu_{T,p(t)})+I(B;R_t)
     <=eta+h_b(r).

Discard the second nonnegative term. Since r<=rho<1/2, binary entropy is increasing on the relevant interval and 1-r>=1-rho. This proves the full-law bound kappa. When r=0 the identity reduces to the unconditioned statement. Absolute continuity and finiteness follow from the same calculation; one may also note q_t^E<=q_t/(1-r).

Disintegrating through the fixed channel C gives exactly

    KL(q_t^E || mu_{T,p(t)})
      =KL(C#q_t^E || C#mu_{T,p(t)})+H_opt(q_t^E).

The retained-marginal term is nonnegative, proving the optimizer conditional bound. The proof is valid for every fixed later t and the estimates are uniform over the displayed interval. E remains the same prefix event in every application.

### Full physical comparison, with evaluator samples retained

Let v=1-sigma_ev^2=1/2, and write d(x)=D x=bar k-bar m. At a fixed matching fiber, put d_y=D y and d_z=D F_M z. The matrix R_ev=D^T D/v preserves W_M and Z_M, so d_y dot d_z=0. Its hidden eigenvalues are 0,4,4.

Let U=(m_ev,k_ev) denote all four model and four belief evaluator samples. At configuration x, the physical evaluator has

    m_ev ~ N(bar m,v I),
    k_ev-m_ev ~ N(0,v I),

with the two noises independent. The recognition evaluator uses the same first law and the increment N(d(x),v I). This is the exact existing coupling, not a new evaluation model.

At a fixed retained state (M,y), define the comparison probability law

    Rbar_y(dz,dU)
      =Pi_{T,Z}(dz) P_ev(dU|y+F_M z)
        exp[(d_y dot (k_ev-m_ev)-|d_y|^2/2)/v].

The multiplier integrates to one for every z by Gaussian square completion. It changes the increment mean from zero to d_y, leaves Pi_{T,Z} as the z marginal, and is a function only of retained y and U. Consequently its conditional law of z given y,U is exactly the physical posterior's hidden conditional; its marginal evaluator law is allowed to differ.

At a fixed z, the recognition evaluator differs from this comparison evaluator only by the increment mean shift d_z. Its KL is |d_z|^2/(2v). Therefore the KL chain rule, first through z and then through U, gives

    H_phys(q | M,y)
      <=KL(q(dz|M,y)||Pi_{T,Z})
          +E_q[|d_z|^2/(2v) | M,y].

All required moments are finite. The original process has a finite second-moment bound, conditioning on an event of probability at least 1-rho preserves finite moments, and both Gaussian reference logarithms are quadratic.

The optimizer hidden law is exactly the tilt

    nu_{T,Z}(dz)
      =Pi_{T,Z}(dz) exp[-|d_z|^2/(2v)] /Z_tilt,
    Z_tilt=(4+T)/(4+5T).

To check its normalizer, each of the two discrepancy coordinates changes rate from 4+T to 4+5T, while the common coordinate is unchanged; the two Gaussian square-root determinant factors multiply to the displayed ratio. Hence

    KL(q_Z||Pi_{T,Z})+E_q |d_z|^2/(2v)
      =KL(q_Z||nu_{T,Z})+log[(4+5T)/(4+T)].

After integrating over retained states, only matching strata contribute; their total probability is at most one. Thus the full physical discarded conditional KL is at most H_opt(q)+log[(4+5T)/(4+T)]. Finally,

    log[(4+5T)/(4+T)]
      =log[1+4T/(4+T)]<=4T/(4+T)<=T.

The physical target is the physical posterior at the original observed records. Only recognition is conditioned on E; this proof does not create a physical path posterior conditioned on E.

### Why learning different parent rows does not alter this loss

The source prior enters a joint density as the factor pi_S. Since S is retained, this factor cancels in every conditional law on a C-fiber. Thus both the hidden optimizer kernel and the evaluator-retained physical hidden kernel are identical for all strictly positive prior rows. Native and parent rows may give different retained source laws and different jump kernels; those differences are dynamical questions. They do not change the static conditional reference or the bound just proved.

Strict positivity matters for this statement: an independently imposed zero prior on an actually occupied stratum would remove its reference support. Ordinary finite-time source learning from positive rows preserves positivity. No masking exception is introduced.

## Why the declared high-probability prefix matters

Even in the exact matching Gaussian nu_T^M, the first hidden coordinate z_1 is independent of the retained state. Its unconditioned hidden KL is zero. Condition instead on the current-state event {z_1>0}, of probability 1/2. The hidden law has density 2 times the Gaussian density on that half-space, so its discarded conditional KL is exactly log 2 for every T. Thus an arbitrary event of probability bounded below need not preserve a vanishing hidden loss. This is an exact example in the same matching fiber, not a numerical observation. Our conclusion uses P(E^c)->0, not merely P(E)>c>0.

Conditioning on a complete realized fine history is a different information regime: it fixes the hidden endpoint. Its conditional law is a Dirac mass, singular relative to the nondegenerate Gaussian fiber, so the hidden KL is infinite. The actual activation here is the complete joint law conditional on the declared event E; it is not a law conditional on the entire realized fine path.

## Scaled and unscaled losses

The mean hidden KL quantities above are dimensionless and unscaled. The optimizer relative-entropy chain discards H_opt, while the scaled optimizer free energy discards exactly T H_opt, hence at most T kappa. With the full evaluator retained, the unscaled physical negative-ELBO drop is H_phys, at most kappa+T, and its T-scaled counterpart is at most T kappa+T^2. The exact coarse laws preserve the same observations and normalization constants.

If the Stage 1 schedule is strengthened to eta,delta<=T and a=T^(1/4), then

    rho<=3T+8sqrt(2/pi)T^(1/4)+3408T^(1/2)
       =O(T^(1/4)),
    kappa=O(T^(1/4)log(1/T)).

This follows from h_b(rho)<=rho log(e/rho) and 1-rho>=1/2 eventually. Consequently both unscaled conditional losses vanish; the scaled losses have an additional factor T. The estimate holds at activation and at every native later marginal in [theta,2s] conditioned on the same completed prefix. It does not require continued coherence to be imposed as a future condition.

## Evidence and unresolved scope

Only the written calculation and the named existing source identities were used. No new external reference, simulation, GPU work, symbolic experiment, or parent-path claim was introduced. The exact marked pushforward and the event-information/physical-tilt calculation supply the static artifact.

The remaining separate obligation is control of an independently evolving parent's retained/source path law from mu_act, with its declared row learning and time interval. Even that would establish a parent for late restored coherence, not the first-block or recursive-formation claim. The original first-episode regime and any subsequent native coalescence remain outside this result.

