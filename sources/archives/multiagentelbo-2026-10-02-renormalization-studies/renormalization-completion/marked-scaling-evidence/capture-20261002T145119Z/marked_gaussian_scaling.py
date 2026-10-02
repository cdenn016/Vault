"""Sparse quenched Gaussian blocking with complete rooted link marks."""
from __future__ import annotations

from dataclasses import dataclass
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import splu

Marks = tuple[np.ndarray, np.ndarray, np.ndarray]


@dataclass(frozen=True)
class GaussianPair:
    """Raw Gaussian measure and carried zero-mean Gaussian probability reference."""
    mean: np.ndarray
    covariance: np.ndarray
    reference_covariance: np.ndarray
    log_mass: float

    @property
    def offset(self) -> float:
        r"""Lebesgue action constant c with integral exp(-E)=exp(log_mass)."""
        d = self.mean.size
        return float(0.5*(self.mean @ np.linalg.solve(self.covariance, self.mean)
                          + d*np.log(2*np.pi) + np.linalg.slogdet(self.covariance)[1])
                     - self.log_mass)

    @property
    def relative_offset(self) -> float:
        r"""Constant of -log(dM/d rho), with both measures pushed together."""
        return float(self.offset - 0.5*self.mean.size*np.log(2*np.pi)
                     - 0.5*np.linalg.slogdet(self.reference_covariance)[1])

    def coarsen(self, P: sparse.spmatrix) -> GaussianPair:
        r"""Push M and rho by y=P x, preserving the raw mass."""
        p = P.toarray()
        return GaussianPair(p @ self.mean, p @ self.covariance @ p.T,
                            p @ self.reference_covariance @ p.T, self.log_mass)


def draw_environment(n_cells: int, seed: int, amplitude: float = 0.05) -> tuple[np.ndarray, np.ndarray]:
    """Draw iid cell pairs with independent bounded GL+(2,R) link perturbations."""
    noise = np.random.default_rng(seed).uniform(-amplitude, amplitude, (n_cells, 2, 2, 2))
    return np.diag([1.4, 0.7]) + noise[:, 0], np.array([[1., .45], [0., 1.]]) + noise[:, 1]


def build_precision(A: np.ndarray, B: np.ndarray, mass: float, kappa: float,
                    gamma: float, eta: float) -> sparse.csc_matrix:
    r"""Principal finite precision of m^2||x||^2 plus the four declared edge energies."""
    n, k = A.shape[:2]
    eye = np.eye(k)
    blocks = []
    for a, b in zip(A, B):
        J = mass*np.eye(2*k)
        for link, weight in ((eye, kappa), (a, gamma), (b, gamma)):
            D = np.c_[eye, -link]
            J += weight*(D.T @ D)
        J[:k, :k] += 2*eta*eye  # Dirichlet exterior retains the infinite diagonal.
        blocks.append(J)
    H = sparse.block_diag(blocks, format="csc")
    rows = np.array([2*k*i+a for i in range(n-1) for a in range(k)], dtype=int)
    cols = rows+2*k
    off = sparse.coo_matrix((-eta*np.ones(2*len(rows)),
                             (np.r_[rows, cols], np.r_[cols, rows])), shape=H.shape)
    return (H+off).tocsc()


def cell_map(n_cells: int, padding: int) -> sparse.csr_matrix:
    r"""Map padded microscopic coordinates to z_i=(r_i+u_i)/sqrt(2)."""
    rows = np.repeat(np.arange(2*n_cells), 2)
    cols = np.array([4*(i+padding)+a+j for i in range(n_cells) for a in range(2) for j in (0, 2)])
    return sparse.csr_matrix((np.ones(4*n_cells)/np.sqrt(2), (rows, cols)),
                             shape=(2*n_cells, 4*(n_cells+2*padding)))


def block_map(frames: np.ndarray, ratio: int) -> sparse.csr_matrix:
    r"""Root-transported normalized sums, P_Ii=G_root G_i^-1/sqrt(b)."""
    n, k = frames.shape[:2]
    if n % ratio:
        raise ValueError("cell count must be divisible by block ratio")
    root = frames[np.arange(n)//ratio*ratio]
    values = root @ np.linalg.inv(frames) / np.sqrt(ratio)
    rows = np.array([k*(i//ratio)+a for i in range(n) for a in range(k) for _ in range(k)])
    cols = np.array([k*i+a for i in range(n) for _ in range(k) for a in range(k)])
    return sparse.csr_matrix((values.ravel(), (rows, cols)), shape=(k*(n//ratio), k*n))


def initial_marks(A: np.ndarray, B: np.ndarray, frames: np.ndarray) -> Marks:
    """All forward/reverse identity, A, B, and neighboring-root copies in stable order."""
    n = len(A)
    ids = np.arange(n)
    inv = np.linalg.inv(frames)
    src, dst, values = [], [], []
    for marks in (np.tile(np.eye(2), (n, 1, 1)), A, B):
        dressed = frames @ marks @ inv
        src.extend([ids, ids]); dst.extend([ids, ids])
        values.extend([dressed, np.linalg.inv(dressed)])
    boundary = frames[1:] @ inv[:-1]
    src.extend([ids[:-1], ids[1:]]); dst.extend([ids[1:], ids[:-1]])
    values.extend([boundary, np.linalg.inv(boundary)])
    return np.concatenate(src), np.concatenate(dst), np.concatenate(values)


def push_marks(marks: Marks, frames: np.ndarray, ratio: int) -> Marks:
    r"""Dress every original edge copy with T_dst M T_src^-1; discard no marks."""
    src, dst, values = marks
    T = frames[np.arange(len(frames))//ratio*ratio] @ np.linalg.inv(frames)
    return src//ratio, dst//ratio, T[dst] @ values @ np.linalg.inv(T[src])


def solve_pair(H: sparse.csc_matrix, P: sparse.csr_matrix, h: np.ndarray,
               mass: float) -> tuple[GaussianPair, float]:
    r"""Compute P H^-1 h, P H^-1 P^T and push rho=N(0,m^-2 I) without dense H^-1."""
    factor = splu(H)
    rhs = np.column_stack([h, P.T.toarray()])
    solved = factor.solve(rhs)
    residual = float(np.max(np.abs(H @ solved-rhs))/max(1., np.max(np.abs(rhs))))
    mu = solved[:, 0]
    covariance = np.asarray(P @ solved[:, 1:])
    log_mass = float(0.5*(len(h)*np.log(2*np.pi)
                           - np.log(np.abs(factor.U.diagonal())).sum() + h @ mu))
    return GaussianPair(np.asarray(P @ mu), covariance, (P @ P.T).toarray()/mass, log_mass), residual


def padded_covariance_bound(mass: float, upper: float, padding: int) -> float:
    r"""Exact-arithmetic ||P(C_infinite-C_pad)P^T|| <= 2 q^(2(p+1))/m^2."""
    return float(2/mass*(1-mass/upper)**(2*(padding+1)))


def susceptibility_reference(H: sparse.csc_matrix, mass: float, upper: float,
                             n_cells: int, padding: int, degree: int) -> tuple[np.ndarray, float]:
    r"""Empirical symmetric row sum via local Neumann polynomial; tail excludes sampling error."""
    if degree >= padding:
        raise ValueError("Neumann degree must be below the padding")
    q = 1-mass/upper
    S = np.c_[np.eye(2), np.eye(2)]/np.sqrt(2)
    term = np.tile(S.T, (n_cells+2*padding, 1))
    total = term/upper
    for _ in range(degree):
        term = term-H @ term/upper
        total = total+term/upper
    rows = np.array([S @ total[4*i:4*i+4] for i in range(padding, padding+n_cells)])
    reference = rows.mean(axis=0)
    tail = q**(degree+1)/upper*((2*degree+3)/(1-q)+2*q/(1-q)**2)
    return (reference+reference.T)/2, float(tail)

