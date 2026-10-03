"""Predeclared joint-channel compressed-message comparison."""
from __future__ import annotations
import os
from pathlib import Path
import subprocess
import sys

RUN={"input_root":"artifacts/gaussian-joint-parent/20261002T161127396348Z","n_paths":2}
THEORY={"n_agents":[512,1024],"block":16,"shortcut_mass":1e-12,"basis":"activation_conditional_joint_channel_sensitivity"}
NUMERICS={"device":"cpu","dtype":"float64","cpu_threads":1}


def main() -> int:
    """Select the existing CPU scientific runtime, then execute one pilot."""
    sequential=os.environ.get("MKL_THREADING_LAYER")=="SEQUENTIAL"
    os.environ["MKL_THREADING_LAYER"]="SEQUENTIAL"
    for key in ("OMP_NUM_THREADS","MKL_NUM_THREADS"):os.environ[key]="1"
    interpreter=Path(os.environ.get("CUDA_PYTHON","C:/anaconda/python.exe"))
    if not sequential or not sys.flags.isolated or Path(sys.executable).resolve()!=interpreter.resolve():
        return subprocess.run([str(interpreter),"-I","-B",str(Path(__file__).resolve())],env=os.environ.copy(),check=False).returncode
    import json,time,traceback,zipfile,hashlib
    from dataclasses import replace,fields
    from datetime import datetime,timezone
    import numpy as np
    import torch
    root=Path(__file__).resolve().parents[1];sys.path.insert(0,str(root/"src"))
    from multiagent_elbo.realizations.gaussian.coupled_learning import CoupledState, free_energy
    from multiagent_elbo.realizations.gaussian.coupled_learning_experiment import build_coupled_case
    from multiagent_elbo.realizations.gaussian.locality import block_mean_projector
    from multiagent_elbo.realizations.gaussian.gaussian_compression import compile_compression
    from multiagent_elbo.realizations.gaussian.joint_informed_compression import joint_informed_basis
    from multiagent_elbo.realizations.gaussian.source_adapted_filter import gaussian_joint_scores
    if NUMERICS!={"device":"cpu","dtype":"float64","cpu_threads":1}:
        raise ValueError("this pilot requires the declared CPU float64 single-thread lane")
    torch.set_num_threads(1)
    base=root/"docs/research/2026-10-02-renormalization-completion"
    native_dir=root/RUN["input_root"];old_dir=base/"source-adapted-evidence"
    native=json.loads((native_dir/"metadata.json").read_text())
    old=json.loads((old_dir/"metadata.json").read_text())
    if native["status"]!="pass" or old["status"]!="pass" or old["run"]["input_root"]!=RUN["input_root"]:
        raise ValueError("completed matching native and baseline studies are required")
    if THEORY["block"]!=old["theory"]["block"] or THEORY["shortcut_mass"]!=old["theory"]["shortcut_mass"]:
        raise ValueError("candidate conventions must match the archived comparison")
    directory=root/"artifacts/gaussian-joint-informed-message"/datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    directory.mkdir(parents=True)
    metadata={"run":RUN,"theory":THEORY,"numerics":NUMERICS,"status":"running","cases":[],
              "python":sys.executable,"python_version":sys.version,"torch":torch.__version__,"cuda_available":torch.cuda.is_available(),
              "base_head":subprocess.check_output(["git","rev-parse","HEAD"],cwd=root,text=True).strip(),
              "working_status":subprocess.check_output(["git","status","--short"],cwd=root,text=True),
              "source_sha256_diagnostic":{},"input_sha256_diagnostic":{},"native_metadata":native,
              "native_resampling":False,"gpu_used":False,"retries":0}
    sources=list((root/"src/multiagent_elbo/realizations/gaussian").glob("*.py"))
    sources += [Path(__file__),root/"tests/test_joint_informed_compression.py",root/"tests/test_source_informed_compression.py",base/"joint-informed-CONTRACT.md"]
    with zipfile.ZipFile(directory/"source.zip","w",zipfile.ZIP_DEFLATED) as z:
        for path in sources:
            rel=str(path.relative_to(root));data=path.read_bytes();z.writestr(rel,data)
            metadata["source_sha256_diagnostic"][rel]=hashlib.sha256(data).hexdigest()
    def save() -> None:
        (directory/"metadata.json").write_text(json.dumps(metadata,indent=2),encoding="utf-8")
    save();started=time.perf_counter();print(str(directory),flush=True)
    try:
        with torch.no_grad():
            for N in THEORY["n_agents"]:
                paths=[root/native["run"]["activation_root"]/f"N{N}-learn_both-final.npz",
                       root/native["run"]["schedule_root"]/f"N{N}-learn_both-schedule.npz",
                       native_dir/f"N{N}-joint-paths-and-scores.npz",old_dir/f"N{N}-source-adapted-scores.npz"]
                for path in paths:metadata["input_sha256_diagnostic"][str(path.relative_to(root))]=hashlib.sha256(path.read_bytes()).hexdigest()
                with np.load(paths[0]) as z:
                    initial=CoupledState(**{k:torch.from_numpy(z[k].copy()) for k in ("mu","Sigma","pi","Theta")})
                with np.load(paths[1]) as z:
                    schedule=tuple(CoupledState(**{k:torch.from_numpy(z[k][t].copy()) for k in ("mu","Sigma","pi","Theta")}) for t in range(native["theory"]["intervals"]))
                schedule=tuple(s for s in schedule for _ in range(native["run"]["substeps"]))
                with np.load(paths[2]) as z:
                    R=torch.from_numpy(z[f"block{THEORY['block']}_paths"][:RUN["n_paths"]].copy())
                    J=torch.from_numpy(z["assignments"][:RUN["n_paths"]].astype(np.int64))
                if len(R)!=RUN["n_paths"]:raise ValueError("missing declared paths")
                with np.load(paths[3]) as z:
                    references={k:z[k][:RUN["n_paths"]].copy() for k in ("gaussian_log_joint","gaussian_log_source","reset_gaussian_log_joint","reset_gaussian_log_source")}
                K=native["theory"]["dimension"];block=THEORY["block"];d=N*K
                P=block_mean_projector(N,K,block)
                model,_=build_coupled_case(N,K,native["run"]["model_seed"],native["theory"]["link_scale"])
                model=replace(model,tau=native["theory"]["tau"])
                Sigma=torch.block_diag(*initial.Sigma)
                dt=native["theory"]["interval_dt"]/native["run"]["substeps"]
                tick=time.perf_counter()
                W,values,channel_diagnostics=joint_informed_basis(initial.mu.flatten(),Sigma,P,initial.Sigma,
                    free_energy(initial,model)[1],dt,native["theory"]["refresh_rate"],len(P),schedule[0],model)
                basis_seconds=time.perf_counter()-tick
                basis_residuals={"whitened_covariance":float((W@Sigma@W.T-torch.eye(len(W),dtype=W.dtype)).abs().max()),
                                 "retained_cross_covariance":float((W@Sigma@P.T).abs().max())}
                np.savez_compressed(directory/f"N{N}-basis.npz",W=W.numpy(),values=values.numpy())
                if max(basis_residuals.values())>1e-9:raise ArithmeticError(f"basis failure: {basis_residuals}")
                tick=time.perf_counter();decoder=compile_compression(initial.mu.flatten(),Sigma,P,W)
                compile_seconds=time.perf_counter()-tick
                case={"n_agents":N,"hidden_rank":len(W),"stored_message_scalars":len(W)+len(W)**2,
                      "decoder_tensor_scalars":sum(getattr(decoder,f.name).numel() for f in fields(decoder)),
                      "dense_reference_mean_covariance_scalars":d+d*d,"retained_coordinates":len(P),"retained_assignment_labels":N,
                      "dense_temporary_covariance_shape":[d,d],"compile_seconds":compile_seconds,"basis_seconds":basis_seconds,"basis_residuals":basis_residuals,"channel_diagnostics":channel_diagnostics,
                      "basis_eigenvalues_min_max":[float(values.min()),float(values.max())],"paths":[]}
                metadata["cases"].append(case);save()
                for b in range(len(R)):
                    half_path=base/"compressed-message-evidence"/f"N{N}-path{b:03d}.npz"
                    metadata["input_sha256_diagnostic"][str(half_path.relative_to(root))]=hashlib.sha256(half_path.read_bytes()).hexdigest()
                    with np.load(half_path) as z:
                        if not np.array_equal(z["R"],R[b:b+1].numpy()) or not np.array_equal(z["assignments"],J[b:b+1].numpy()):
                            raise ValueError("half-block control must use identical retained inputs")
                        half={"half_block_"+k:z[k].copy() for k in ("log_joint","log_source")}
                    source_path=base/"source-informed-evidence"/f"N{N}-path{b:03d}.npz"
                    metadata["input_sha256_diagnostic"][str(source_path.relative_to(root))]=hashlib.sha256(source_path.read_bytes()).hexdigest()
                    with np.load(source_path) as z:
                        if not np.array_equal(z["R"],R[b:b+1].numpy()) or not np.array_equal(z["assignments"],J[b:b+1].numpy()):
                            raise ValueError("source-only control must use identical retained inputs")
                        source_only={"source_only_"+k:z[k].copy() for k in ("log_joint","log_source")}
                    metadata["active"]={"n_agents":N,"path":b};save();tick=time.perf_counter()
                    scored=gaussian_joint_scores(R[b:b+1],J[b:b+1],initial.Sigma,initial,schedule,model,dt,block,
                        refresh_rate=native["theory"]["refresh_rate"],shortcut_mass=THEORY["shortcut_mass"],compression=decoder)
                    elapsed=time.perf_counter()-tick
                    arrays={k:scored[k].numpy() for k in ("log_joint","log_source","source_updates","shortcut")}
                    arrays.update({k:v[b:b+1] for k,v in references.items()});arrays.update(half);arrays.update(source_only)
                    arrays.update({"R":R[b:b+1].numpy(),"assignments":J[b:b+1].numpy()})
                    np.savez_compressed(directory/f"N{N}-path{b:03d}.npz",**arrays)
                    if any(not np.isfinite(v).all() for v in arrays.values()):raise ArithmeticError("nonfinite pilot output")
                    residuals={k:float(scored[k]) for k in ("projection_max_error","covariance_projection_max_error")}
                    if max(residuals.values())>1e-9:raise ArithmeticError(f"observation fiber failure: {residuals}")
                    first=max(abs(float(arrays[k][0,0]-arrays['gaussian_'+k][0,0])) for k in ("log_joint","log_source"))
                    if first>1e-8:raise ArithmeticError(f"activation score mismatch: {first}")
                    contrasts={}
                    for arm in ("gaussian","reset_gaussian","half_block","source_only"):
                        joint=float((arrays[arm+"_log_joint"]-arrays["log_joint"]).sum())
                        source=float((arrays[arm+"_log_source"]-arrays["log_source"]).sum())
                        contrasts[arm]={"joint":joint,"source":source,"configuration":joint-source}
                    record={"path":b,"elapsed_seconds":elapsed,"assignment_changes":int((J[b,1:]!=J[b,:-1]).any(-1).sum()),
                            "source_updates":int(scored["source_updates"].sum()),"activation_score_error":first,
                            "residuals":residuals,"compressed_minus_reference_loss":contrasts}
                    case["paths"].append(record);save();print(json.dumps({"N":N,**record}),flush=True)
            metadata["status"]="pass";metadata.pop("active",None)
    except Exception:
        metadata["status"]="failed";metadata["traceback"]=traceback.format_exc();raise
    finally:
        metadata["elapsed_seconds"]=time.perf_counter()-started;save()
        print(json.dumps({"run_dir":str(directory),"status":metadata["status"],"elapsed_seconds":metadata["elapsed_seconds"]}),flush=True)
    return 0


if __name__=="__main__":raise SystemExit(main())
