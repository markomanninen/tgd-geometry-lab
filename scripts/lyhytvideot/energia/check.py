"""Tests of the exact models that energia.py draws.

    uv run --no-project --python 3.12 --with numpy --with sympy python check.py

1.  The Lemaître-Tolman-Bondi metric of model.py solves Einstein's equations for dust, G^mu_nu = 8 pi G rho u^mu u_nu,
    for any bang time t_B(r).  The time translation and the translations of the picture are not Killing vectors,
    and the rotation is.
2.  The surface of model.py is an extremal of the volume action, its coordinates are conformal, the part of the
    time translation along the surface is X_tau / Omega, and the energy through every time slice is the same.
"""
import numpy as np
import sympy as sp

import model as m


def check(name, ok):
    print(("ok    " if ok else "FAIL  ") + name)
    assert ok, name


# ---- 1. Lemaître-Tolman-Bondi dust

t, r, th, ph = sp.symbols("t r theta phi", positive=True)
tB = sp.Function("t_B")(r)
R = r * (t - tB) ** sp.Rational(2, 3)
Rp = sp.diff(R, r)
co = (t, r, th, ph)
g = sp.diag(1, -Rp ** 2, -R ** 2, -R ** 2 * sp.sin(th) ** 2)
gi = g.inv()
Gam = [[[sum(gi[a, d] * (sp.diff(g[d, b], co[c]) + sp.diff(g[d, c], co[b]) - sp.diff(g[b, c], co[d])) for d in range(4)) / 2
         for c in range(4)] for b in range(4)] for a in range(4)]


def riemann(a, b, c, d):
    return (sp.diff(Gam[a][b][d], co[c]) - sp.diff(Gam[a][b][c], co[d])
            + sum(Gam[a][c][e] * Gam[e][b][d] - Gam[a][d][e] * Gam[e][b][c] for e in range(4)))


ric = sp.Matrix(4, 4, lambda b, d: sum(riemann(a, b, a, d) for a in range(4)))
scal = sum(gi[b, d] * ric[b, d] for b in range(4) for d in range(4))
ein = (gi * (ric - scal * g / 2))                   # G^mu_nu
rho8 = sp.Rational(4, 3) * r ** 2 / (R ** 2 * Rp)   # 8 pi G rho for M(r) = 2 r^3 / (9 G)
num = {tB: 2 * sp.exp(-r ** 2 / 4)}
worst = 0
for a in range(4):
    for b in range(4):
        want = rho8 if a == b == 0 else 0
        f = sp.lambdify((t, r, th), (ein[a, b] - want).subs(num).doit(), "mpmath")
        for pt in ((2.0, .7, 1.1), (3.2, 1.8, .6), (4.7, 3.3, 1.4)):
            worst = max(worst, abs(complex(f(*pt))))
check(f"LTB metric solves Einstein's equations for dust, greatest deviation {worst:.1e}", worst < 1e-9)

lie_t = sp.simplify(sp.diff(g, t).subs(num).doit())
check("the time translation is not a Killing vector of the LTB metric", lie_t != sp.zeros(4, 4))
check("the rotation is a Killing vector of the LTB metric", sp.diff(g, ph) == sp.zeros(4, 4))
# a translation of the picture: the metric at (x + d, y) against the metric at (x, y), through the light cones
s1, s2 = m.ltb_slopes(1.0, 1.5, -1.5), m.ltb_slopes(3.0, 1.5, -1.5)
check("the light cones of the LTB metric differ from place to place", abs(s1[1] - s2[1]) > .2)
s1, s2 = m.ltb_slopes(1.0, 1.5, -1.5), m.ltb_slopes(1.0, 1.5, 0.0)
check("the light cones of the LTB metric differ from time to time", abs(s1[0] - s2[0]) > .2)
check("far from the middle at t = 0 the light cone is the flat one", abs(m.ltb_slopes(40.0, 0, 0)[0] - 1) < 1e-6
      and abs(m.ltb_slopes(40.0, 0, 0)[1] - 1) < 1e-6)

# ---- 2. the surface

rng = np.random.default_rng(3)
pts = [(rng.uniform(-3, 3), rng.uniform(-1.6, 1.6)) for _ in range(400)]
d = 1e-4
dev = dict(gauge=0, wave=0, par=0, null=0, tang=0)
for s, u in pts:
    xt, xs, om = m.X_tau(s, u), m.X_sig(s, u), m.omega(s, u)
    dev["tang"] = max(dev["tang"], np.abs((m.X(s, u + d) - m.X(s, u - d)) / (2 * d) - xt).max(),
                      np.abs((m.X(s + d, u) - m.X(s - d, u)) / (2 * d) - xs).max())
    dev["gauge"] = max(dev["gauge"], abs(m.h(xt, xs)), abs(m.h(xt, xt) - om), abs(m.h(xs, xs) + om))
    # sqrt(g) g^(alpha beta) is diag(1, -1) in conformal coordinates, so the field equation is the wave equation
    box = (m.X_tau(s, u + d) - m.X_tau(s, u - d)) / (2 * d) - (m.X_sig(s + d, u) - m.X_sig(s - d, u)) / (2 * d)
    dev["wave"] = max(dev["wave"], np.abs(box).max())
    xi = np.array([0, 0, 1.0])
    par = m.xi_par(s, u)
    dev["par"] = max(dev["par"], abs(m.h(xi - par, xt)), abs(m.h(xi - par, xs)))
    n1, n2 = m.nulls(s, u)
    dev["null"] = max(dev["null"], abs(m.h(n1, n1)), abs(m.h(n2, n2)))
check(f"the tangent vectors of model.py are the derivatives of X, deviation {dev['tang']:.1e}", dev["tang"] < 1e-5)
check(f"the coordinates are conformal with the factor Omega, deviation {dev['gauge']:.1e}", dev["gauge"] < 1e-12)
check(f"the surface is an extremal of the volume action, deviation {dev['wave']:.1e}", dev["wave"] < 1e-6)
check(f"X_tau / Omega is the part of the time translation along the surface, deviation {dev['par']:.1e}",
      dev["par"] < 1e-12)
check(f"the marks on the surface are light-like in H, deviation {dev['null']:.1e}", dev["null"] < 1e-12)

# the energy through a slice t = constant between two flow lines: the integral of J^tau = h(xi, X_tau) over sigma,
# and the same number from the geometry of the slice, the integral of h(xi_par, n) dl with the unit normal n of the
# slice inside the surface
sig = np.linspace(-3.4, 3.4, 4001)
flux = []
for u in np.linspace(-1.6, 1.6, 9):
    xt = np.array([m.X_tau(s, u) for s in sig])
    xs = np.array([m.X_sig(s, u) for s in sig])
    om = m.omega(sig, u)
    n = xt / np.sqrt(om)[:, None]                   # unit normal of the slice inside the surface
    dl = np.sqrt(om)                                # length of the slice for each unit of sigma
    par = xt / om[:, None]
    dens = np.array([m.h(p, q) for p, q in zip(par, n)]) * dl
    flux.append(np.sum(.5 * (dens[1:] + dens[:-1]) * np.diff(sig)))
check(f"the energy through nine time slices is the same, {min(flux):.6f} to {max(flux):.6f}",
      max(flux) - min(flux) < 1e-9 and abs(flux[0] - 6.8) < 1e-9)
print(f"height of one pulse {m.a_s(0) / 2:.3f}, of the two together {m.a_s(0):.3f}, "
      f"greatest speed of a point of the surface {np.sin(m.PHI / 2):.3f}")

# ---- 3. the pseudotensor energy of pseudo.py

import pseudo  # noqa: E402

e0 = pseudo.ll_energy(pseudo.flat_metric)
check(f"the Landau-Lifshitz energy of flat space in Cartesian coordinates is zero, {e0:.1e}", abs(e0) < 1e-10)
eS = pseudo.ll_energy(pseudo.schwarzschild_isotropic(.1), rho=40)
check(f"the Landau-Lifshitz energy of a Schwarzschild mass 0,1 at radius 40 is {eS:.4f}", abs(eS - .1) < .002)
ed = pseudo.ll_energy(pseudo.ltb_metric)
er = [pseudo.ll_energy(pseudo.renamed(pseudo.ltb_metric, 1.0, ph)) for ph in np.linspace(0, 2 * np.pi, 9)[:-1]]
check(f"the dust energy depends on the names of the points, {ed:.4f} and renamed {min(er):.4f} to {max(er):.4f}",
      max(er) - min(er) > .5 * abs(ed))
