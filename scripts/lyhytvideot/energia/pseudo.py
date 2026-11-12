"""The Landau-Lifshitz energy of the dust solution of model.py, in the picture's coordinates and in renamed ones.

Einstein and later Landau and Lifshitz tried to rescue the total energy of general relativity by adding to the
energy-momentum tensor T a pseudotensor t of the gravitational field, such that the sum has an ordinary divergence
that vanishes,

    d_mu [ (-g) (T^{mu nu} + t^{mu nu}) ] = 0.

The total is then a surface integral of the superpotential (Landau and Lifshitz, The Classical Theory of Fields,
section 96, signature (+,-,-,-), G = c = 1),

    P^0 = oint h^{00 a} dS_a,    h^{00 a} = 1/(16 pi) d_m [ (-g) (g^{00} g^{am} - g^{0a} g^{0m}) ].

The sum T + t is not a tensor, so the number depends on the coordinates.  The video shows this: the lattice lines
wander (energia.py, function wander), the events stay where they are, and the number changes.

The coordinates of the picture are (t, x, y) with z = 0, and the dust solution of model.py is spherical, so the
fourth coordinate z is added here as the third comoving Cartesian coordinate.  The renaming of energia.py changes
x, y and t and leaves z alone.
"""
import numpy as np

import model as m

FD = 1e-4                                   # step of the finite differences


def ltb_metric(c):
    """The covariant metric of the dust solution at points c = (t, x, y, z), comoving Cartesian coordinates.

    ds^2 = dt^2 - (R^2/r^2) |dx|^2 - (R'^2 - R^2/r^2) (n . dx)^2, with R and R' of model.py, t measured from
    T_REF as in the picture.  The overall factor LAM^2 = T_REF^(4/3) is divided out, so that far from the middle
    the spatial metric at t = 0 is the flat one, as the light cones of the picture assume.
    """
    t, xs = c[..., 0], c[..., 1:]
    r = np.linalg.norm(xs, axis=-1)
    n = xs / r[..., None]
    u = m.T_REF + t - m.t_bang(r)
    r_dtb = -2 * r * r / m.W ** 2 * m.t_bang(r)
    R_over_r = u ** (2 / 3)
    Rp = u ** (2 / 3) - (2 / 3) * r_dtb * u ** (-1 / 3)
    a2, b2 = R_over_r ** 2 / m.LAM ** 2, Rp ** 2 / m.LAM ** 2
    g = np.zeros(c.shape[:-1] + (4, 4))
    g[..., 0, 0] = 1
    eye = np.eye(3)
    g[..., 1:, 1:] = -(a2[..., None, None] * eye + (b2 - a2)[..., None, None] * n[..., :, None] * n[..., None, :])
    return g


def flat_metric(c):
    g = np.zeros(c.shape[:-1] + (4, 4))
    g[..., 0, 0], g[..., 1, 1], g[..., 2, 2], g[..., 3, 3] = 1, -1, -1, -1
    return g


def schwarzschild_isotropic(M):
    def g_of(c):
        rho = np.linalg.norm(c[..., 1:], axis=-1)
        q = M / (2 * rho)
        g = np.zeros(c.shape[:-1] + (4, 4))
        g[..., 0, 0] = ((1 - q) / (1 + q)) ** 2
        for i in (1, 2, 3):
            g[..., i, i] = -(1 + q) ** 4
        return g
    return g_of


def picture_wander(amp, ph):
    """The renaming of energia.py as a map from new coordinates c to old coordinates x = c + amp W(c), with its
    Jacobian dx/dc.  The picture's three directions (x, y, t) are the components (1, 2, 0) here."""
    def old(c):
        t, x, y = c[..., 0], c[..., 1], c[..., 2]
        d = np.zeros_like(c)
        d[..., 1] = .3 * np.sin(1.3 * y + 1.1 * t + ph)
        d[..., 2] = .3 * np.sin(.9 * x - 1.2 * t + 1.7 * ph)
        d[..., 0] = .3 * np.sin(.8 * x + 1.4 * y + .6 * ph)
        return c + amp * d

    def jac(c):
        t, x, y = c[..., 0], c[..., 1], c[..., 2]
        J = np.zeros(c.shape[:-1] + (4, 4)) + np.eye(4)
        cx = .3 * np.cos(1.3 * y + 1.1 * t + ph)
        cy = .3 * np.cos(.9 * x - 1.2 * t + 1.7 * ph)
        ct = .3 * np.cos(.8 * x + 1.4 * y + .6 * ph)
        J[..., 1, 2] += amp * 1.3 * cx
        J[..., 1, 0] += amp * 1.1 * cx
        J[..., 2, 1] += amp * .9 * cy
        J[..., 2, 0] += amp * -1.2 * cy
        J[..., 0, 1] += amp * .8 * ct
        J[..., 0, 2] += amp * 1.4 * ct
        return J

    return old, jac


def renamed(g_old, amp, ph):
    """The metric in the new coordinates: g'_{mu nu}(c) = J^a_mu J^b_nu g_ab(x(c))."""
    old, jac = picture_wander(amp, ph)

    def g_of(c):
        J = jac(c)
        return np.einsum("...am,...ab,...bn->...mn", J, g_old(old(c)), J)
    return g_of


def superpotential(g_of, c):
    """(-g) (g^{00} g^{am} - g^{0a} g^{0m}) at the points c, for spatial a and m."""
    g = g_of(c)
    gi = np.linalg.inv(g)
    det = -np.linalg.det(g)
    return det[..., None, None] * (gi[..., 0, 0, None, None] * gi[..., 1:, 1:]
                                   - gi[..., 0, 1:, None] * gi[..., 0, None, 1:])


def ll_energy(g_of, t0=0.0, rho=2.5, nth=48, nph=96):
    """The Landau-Lifshitz energy inside the coordinate sphere |x| = rho at the coordinate time t0."""
    th = (np.arange(nth) + .5) * np.pi / nth
    ph = (np.arange(nph) + .5) * 2 * np.pi / nph
    TH, PH = np.meshgrid(th, ph, indexing="ij")
    n = np.stack([np.sin(TH) * np.cos(PH), np.sin(TH) * np.sin(PH), np.cos(TH)], axis=-1)
    c = np.concatenate([np.full(TH.shape + (1,), t0), rho * n], axis=-1)
    h = np.zeros(TH.shape + (3,))                    # h^{00 a} * 16 pi
    for mm in range(3):
        e = np.zeros(4)
        e[mm + 1] = FD
        dS = (superpotential(g_of, c + e) - superpotential(g_of, c - e)) / (2 * FD)
        h += dS[..., :, mm]
    flux = np.einsum("...a,...a->...", h, n)
    dA = rho * rho * np.sin(TH) * (np.pi / nth) * (2 * np.pi / nph)
    return float((flux * dA).sum() / (16 * np.pi))


if __name__ == "__main__":
    print("flat, Cartesian      ", round(ll_energy(flat_metric), 8))
    for M, R in ((.1, 20), (.1, 40)):
        print(f"Schwarzschild M={M} r={R} ", round(ll_energy(schwarzschild_isotropic(M), rho=R), 5))
    print("dust, picture coords ", round(ll_energy(ltb_metric), 4))
    for ph in np.linspace(0, 2 * np.pi, 9)[:-1]:
        print(f"dust, renamed ph={ph:.2f}", round(ll_energy(renamed(ltb_metric, 1.0, ph)), 4))
    print("flat, renamed        ", round(ll_energy(renamed(flat_metric, 1.0, .7)), 4))
