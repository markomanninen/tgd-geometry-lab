#!/usr/bin/env python3
"""Kahler current and mean curvature on a lattice, independent of the Maxima library.

Every derivative of the map, the metric and the current is a 4th-order finite
difference.  The surfaces depend on three of the four coordinates, and the fourth
enters through the constant part of the metric.  The current uses J(CP2) alone and
is j^b = d_a(sqrt|g| J^ab)/sqrt|g|.  The printed norm is taken at the centre of the
lattice, so it should settle as N grows, and max|H| should fall towards zero as
h^4 on a minimal surface.

    uv run -q --no-project --with numpy python scripts/lattice_kahler_current.py
"""
import numpy as np

def d(f, h, axis):
    """4th-order central difference, interior points only are meaningful."""
    return (np.roll(f, 2, axis) * 1 - 8 * np.roll(f, 1, axis)
            + 8 * np.roll(f, -1, axis) - np.roll(f, -2, axis)) / (12 * h)

def fs_hermitian(z1, z2):
    """s_ij = d_i dbar_j log(1+|z|^2), ds^2 = s_ij dz^i dzbar^j"""
    q = 1 + abs(z1) ** 2 + abs(z2) ** 2
    s = np.empty(z1.shape + (2, 2), complex)
    zb = [np.conj(z1), np.conj(z2)]
    zz = [z1, z2]
    for i in range(2):
        for j in range(2):
            s[..., i, j] = (1.0 * (i == j)) / q - zb[i] * zz[j] / q ** 2
    return s

def run(name, grid, m_metric, z1f, z2f, scalars):
    """grid: list of (index in 0..3, array of values) for the three lattice
    axes, m_metric(X): 4x4 M^4 metric, z1f, z2f(X): CP2 coordinates,
    scalars(X): gradients d_b f of M^4 embedding functions."""
    axes = [g[0] for g in grid]
    hs = [g[1][1] - g[1][0] for g in grid]
    mesh = np.meshgrid(*[g[1] for g in grid], indexing='ij')
    miss = ({0, 1, 2, 3} - set(axes)).pop()
    X = [None] * 4
    for a, m in zip(axes, mesh):
        X[a] = m
    X[miss] = np.zeros_like(mesh[0])
    z = [z1f(X), z2f(X)]
    # first derivatives of the map on the lattice
    dz = np.zeros((2, 4) + mesh[0].shape, complex)
    dzb = np.zeros((2, 4) + mesh[0].shape, complex)
    for k in range(2):
        for ia, a in enumerate(axes):
            dz[k, a] = d(z[k], hs[ia], ia)
            dzb[k, a] = d(np.conj(z[k]), hs[ia], ia)
    s = fs_hermitian(z[0], z[1])
    P = np.zeros(mesh[0].shape + (4, 4), complex)
    for a in range(4):
        for b in range(4):
            P[..., a, b] = sum(s[..., i, j] * dz[i, a] * dzb[j, b]
                               for i in range(2) for j in range(2))
    # CP2 enters with the negative sign of H = M^4 x CP2
    g = m_metric(X) - (P + np.swapaxes(P, -1, -2)).real / 2
    J = (1j * (P - np.swapaxes(P, -1, -2))).real / 2
    gi = np.linalg.inv(g)
    sg = np.sqrt(np.abs(np.linalg.det(g)))
    Ju = gi @ J @ gi
    SJ = sg[..., None, None] * Ju
    # j^b = d_a(sqrt g J^ab)/sqrt g
    j = np.zeros(mesh[0].shape + (4,))
    for b in range(4):
        for ia, a in enumerate(axes):
            j[..., b] += d(SJ[..., a, b], hs[ia], ia)
        j[..., b] /= sg
    # mean curvature, CP2 components: Laplacian + Christoffel term
    Hz = []
    for k in range(2):
        flux = [sum(sg * gi[..., a, b] * dz[k, b] for b in range(4)) for a in range(4)]
        lap = sum(d(flux[a], hs[ia], ia) for ia, a in enumerate(axes)) / sg
        q = 1 + abs(z[0]) ** 2 + abs(z[1]) ** 2
        zb = [np.conj(z[0]), np.conj(z[1])]
        # Gamma^k_jl = -(delta^k_j zb_l + delta^k_l zb_j)/q on CP2
        ch = 0
        for jj in range(2):
            for l in range(2):
                G = -((k == jj) * zb[l] + (k == l) * zb[jj]) / q
                ch = ch + G * sum(gi[..., a, b] * dz[jj, a] * dz[l, b]
                                  for a in range(4) for b in range(4))
        Hz.append(lap + ch)
    # mean curvature, M^4 components: Laplacian of the Cartesian functions
    Hm = []
    for grad in scalars(X):
        flux = [sum(sg * gi[..., a, b] * grad[b] for b in range(4)) for a in range(4)]
        Hm.append(sum(d(flux[a], hs[ia], ia) for ia, a in enumerate(axes)) / sg)
    cut = tuple(slice(4, -4) for _ in axes)
    jm = np.max(np.abs(j[cut]))
    hmax = max(np.max(np.abs(x[cut])) for x in Hz + Hm)
    n = len(grid[0][1])
    c = (n - 1) // 2
    print(f"{name:34s} N={n:4d}  |j| at centre={np.linalg.norm(j[c, c, c]):.8f}  max|H|={hmax:11.4e}")
    return j, mesh

m_flat = lambda X: np.broadcast_to(np.array([[0, .5, 0, 0], [.5, 0, 0, 0],
                                            [0, 0, -1, 0], [0, 0, 0, -1.]]),
                                   X[0].shape + (4, 4))
def m_sph(X):
    r, a, b = X[1], X[2], X[3]
    f = (2 * r / (1 + a ** 2 + b ** 2)) ** 2
    m = np.zeros(X[0].shape + (4, 4))
    m[..., 0, 0] = 1; m[..., 1, 1] = -1; m[..., 2, 2] = -f; m[..., 3, 3] = -f
    return m

def flat_scalars(X):
    e = lambda i: [np.full(X[0].shape, 1.0 * (i == k)) for k in range(4)]
    return [e(0), e(1), e(2), e(3)]

def sph_scalars(X):
    # Cartesian x, y, z = r n(a,b) with stereographic n, gradients analytic
    r, a, b = X[1], X[2], X[3]
    q = 1 + a ** 2 + b ** 2
    nx, ny, nz = 2 * a / q, 2 * b / q, (a ** 2 + b ** 2 - 1) / q
    zero = np.zeros_like(r)
    def g(n, na, nb):
        return [zero, n, r * na, r * nb]
    return [[np.ones_like(r), zero, zero, zero],
            g(nx, 2 / q - 4 * a ** 2 / q ** 2, -4 * a * b / q ** 2),
            g(ny, -4 * a * b / q ** 2, 2 / q - 4 * b ** 2 / q ** 2),
            g(nz, 4 * a / q ** 2, 4 * b / q ** 2)]

def m_cyl(X):
    m = np.zeros(X[0].shape + (4, 4))
    m[..., 0, 0] = 1; m[..., 1, 1] = -1; m[..., 2, 2] = -X[1] ** 2; m[..., 3, 3] = -1
    return m

def cyl_scalars(X):
    # Cartesian t, x, y, z in the chart (t, rho, phi, z)
    r, f = X[1], X[2]
    o = np.zeros_like(r); e = np.ones_like(r)
    return [[e, o, o, o], [o, np.cos(f), -r * np.sin(f), o],
            [o, np.sin(f), r * np.cos(f), o], [o, o, o, e]]

def cyl_axes(n):
    return [(1, np.linspace(1., 2., n)), (2, np.linspace(.1, 1.1, n)), (3, np.linspace(.1, 1.1, n))]

zero = lambda X: np.zeros_like(X[0], complex)
def flat_axes(n):
    return [(0, np.linspace(.3, 1.3, n)), (2, np.linspace(.2, 1.2, n)), (3, np.linspace(.2, 1.2, n))]
def sph_axes(n):
    return [(1, np.linspace(1., 2., n)), (2, np.linspace(.1, 1.1, n)), (3, np.linspace(.1, 1.1, n))]
w_f = lambda X: X[2] + 1j * X[3]
w_s = lambda X: X[2] + 1j * X[3]

cases = [
  ("flat  xi1 = w/2",          flat_axes, m_flat, lambda X: w_f(X) / 2, zero, flat_scalars),
  ("flat  xi1 = w^2",          flat_axes, m_flat, lambda X: w_f(X) ** 2, zero, flat_scalars),
  ("flat  xi1 = u w",          flat_axes, m_flat, lambda X: X[0] * w_f(X), zero, flat_scalars),
  ("flat  xi1 = u^2 (f(u))",   flat_axes, m_flat, lambda X: X[0] ** 2 + 0j, zero, flat_scalars),
  ("sph   xi1 = w (line)",     sph_axes, m_sph, w_s, zero, sph_scalars),
  ("sph   xi1 = sqrt2 w, w^2", sph_axes, m_sph, lambda X: np.sqrt(2) * w_s(X), lambda X: w_s(X) ** 2, sph_scalars),
  ("sph   xi1 = 2 w",          sph_axes, m_sph, lambda X: 2 * w_s(X), zero, sph_scalars),
  ("sph   xi1 = w^2",          sph_axes, m_sph, lambda X: w_s(X) ** 2, zero, sph_scalars),
  ("cyl   xi1 = (z + i phi)/2", cyl_axes, m_cyl, lambda X: (X[3] + 1j * X[2]) / 2, zero, cyl_scalars),
]
for name, ax, m, z1, z2, sc in cases:
    for n in (25, 49, 97):
        run(name, ax(n), m, z1, z2, sc)
    print()

# closed form for xi1 = w/2 in the (x,y) plane: g = -Omega (dx^2+dy^2), J_xy = omega,
# so |j^y| = |d_x(omega/Omega)|/Omega and |j^x| = |d_y(omega/Omega)|/Omega
def closed_form(x, y):
    q = 1 + (x ** 2 + y ** 2) / 4
    Om = 1 + 1 / (4 * q ** 2)
    return np.array([abs(v) / (4 * q ** 3 * Om ** 3) for v in (y, x)])

j, mesh = run("flat  xi1 = w/2", flat_axes(97), m_flat, lambda X: w_f(X) / 2, zero, flat_scalars)
i = (48, 40, 56)
px, py = mesh[1][i], mesh[2][i]
print(f"point ({px:.4f}, {py:.4f})  lattice |j^x|, |j^y| = {abs(j[i][2]):.9f}, {abs(j[i][3]):.9f}"
      f"  closed form = {closed_form(px, py)[0]:.9f}, {closed_form(px, py)[1]:.9f}")
