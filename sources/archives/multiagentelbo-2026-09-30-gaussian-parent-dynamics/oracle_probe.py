"""Bounded native-call discriminator; reproduces only the oracle input."""
import json,sys
import numpy as np
import scipy,scipy.linalg,scipy.stats
if sys.argv[1]=="torch-package":
 import torch
 torch.set_num_threads(1)
 from multiagent_elbo.realizations.gaussian.network_dynamics import ou_transition
 print("torch and package imported",flush=True)
J=np.array([[2.3,-0.4,0.2],[-0.4,1.7,-0.3],[0.2,-0.3,1.4]])
L=np.array([[1.1,0,0],[0.3,0.8,0],[-0.1,0.2,0.9]])
M=L@L.T
A=-M@J
block=np.block([[A,2*M],[np.zeros_like(A),-A.T]])*0.27
print(json.dumps({"arm":sys.argv[1],"scipy":scipy.__version__,"numpy":np.__version__,"shape":block.shape,"max_abs":float(np.abs(block).max())}),flush=True)
value=scipy.linalg.expm(block)
print(json.dumps({"finite":bool(np.isfinite(value).all()),"trace":float(np.trace(value))}),flush=True)
