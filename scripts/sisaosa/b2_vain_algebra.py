# Coordinate and tangent-space checks that do not use the O'Neill formula.
import sympy as sp, random, itertools
from a_homogeeninen import Homog, ip, normalise, E, su3, I


print("== 3. vertical curvature of F -> CP2 is anti-self-dual, not J ==")
m, hh = su3()
m = [normalise(x) for x in m]
y = sp.Symbol("y", positive=True)
F = Homog(m, [1, 1, 1, 1, y, y], hh)
for k in (4, 5):
    print("V component", k, ":", {(i, j): F.c[i][j][k] for i in range(4) for j in range(i + 1, 4) if F.c[i][j][k] != 0})
Mh = {(i, j): F.hpart[i][j][4, 5] for i in range(4) for j in range(i + 1, 4) if F.hpart[i][j][4, 5] != 0}
print("rotation of the fibre tangent plane about u (third curvature form):", Mh)
print("base J = e01+e23 (both root planes with the same sign)")


# tangent-space identities
def form(pairs, n=4):
    M = sp.zeros(n)
    for (i, j), c in pairs.items():
        M[i, j] = c
        M[j, i] = -c
    return M


s0 = {"minus1": form({(0, 1): 1, (2, 3): -1}), "minus2": form({(0, 2): 1, (1, 3): 1}), "minus3": form({(0, 3): 1, (1, 2): -1})}
sJ = form({(0, 3): 1, (1, 2): 1})
sp2 = form({(0, 1): 1, (2, 3): 1})
sp3 = form({(0, 2): 1, (1, 3): -1})
print("book forms in frame e0..e3: R01=e01-e23, R02=e02-e31=e02+e13, R03=4e03+2e12")
R03 = form({(0, 3): 4, (1, 2): 2})
print("R03 - 3(e03+e12) equals e03-e12:", R03 - 3 * sJ == s0["minus3"])
eps = lambda M: sp.Matrix(4, 4, lambda i, j: sum(sp.LeviCivita(i, j, k, l) * M[k, l] for k in range(4) for l in range(4)) / 2)
print("ASD:", [eps(v) == -v for v in s0.values()], " J, phi1, phi2 SD:", eps(sJ) == sJ, eps(sp2) == sp2, eps(sp3) == sp3)
print("orthogonal to J:", [(v.T * sJ).trace() for v in s0.values()])

import numpy as np
rng = np.random.default_rng(1)
sig = [np.array(v.tolist(), dtype=float) for v in s0.values()]
sjn, p1, p2 = [np.array(v.tolist(), dtype=float) for v in (sJ, sp2, sp3)]
worst = 0
for _ in range(200):
    L = rng.normal(size=(4, 4))
    eta = np.diag([1, -1, -1, -1.0])
    g4 = eta - L.T @ L  # induced metric in (+,-,-,-), CP2 part negative
    gi = np.linalg.inv(g4)
    def sq(w):
        P = L.T @ w @ L
        return np.trace(gi @ P @ gi @ P.T)
    Q = sum(sq(w) for w in sig)
    Qp = sq(sjn) + sq(p1) + sq(p2)
    T = gi @ (-(L.T @ L))
    worst = max(worst, abs(Q - ((np.trace(T))**2 - np.trace(T @ T))), abs(Q - Qp))
print("max |Q-(trT^2-trT.T)|, |Q+-Q-| over random tangent maps, Lorentzian g:", worst)


def example(name, L):
    g4 = np.eye(4) + L.T @ L
    gi = np.linalg.inv(g4)
    sq = lambda w: np.trace(gi @ (L.T @ w @ L) @ gi @ (L.T @ w @ L).T)
    print(name, "Q=%.4f K=%.4f |Pphi|^2=%.4f" % (sum(sq(w) for w in sig), sq(sjn), sq(p1) + sq(p2)))


e_ = lambda i, j: np.outer(np.eye(4)[i], np.eye(4)[j])
print("g = 1 + L^T L, unit-slope examples, CP2 frame with J=e03+e12:")
example("rank 1            ", e_(0, 0))
example("rank 2 complex 03 ", e_(0, 0) + e_(3, 1))
example("rank 2 Lagrangian ", e_(0, 0) + e_(1, 1))
example("rank 4            ", np.eye(4))
print("CP2-type limit, g=L^T L only: Q=12 K=4 (trT=4, trT^2=4)")

print("== 4. first variation of the term on a complex curve in E^2 x CP1 ==")
x, yy = sp.symbols("x y", real=True)
u1 = sp.Function("u1")(x, yy)
u2 = sp.Function("u2")(x, yy)


def EL(Lag, fields, tests):
    out = []
    for f in fields:
        v = sp.diff(Lag, f)
        for c in (x, yy):
            v -= sp.diff(sp.diff(Lag, sp.Derivative(f, c)), c)
        out.append(v)
    res = []
    for v in out:
        w = v.subs({u1: tests[0], u2: tests[1]}).doit()
        res.append(sp.simplify(w))
    return res


lam = 1 / (1 + u1**2 + u2**2)**2
d = lambda f, c: sp.Derivative(f, c)
Pxx = lam * (d(u1, x)**2 + d(u2, x)**2)
Pyy = lam * (d(u1, yy)**2 + d(u2, yy)**2)
Pxy = lam * (d(u1, x) * d(u1, yy) + d(u2, x) * d(u2, yy))
detP = Pxx * Pyy - Pxy**2
detg = (1 + Pxx) * (1 + Pyy) - Pxy**2
for nm, t in (("f=w", (x, yy)), ("f=w^2", (x**2 - yy**2, 2 * x * yy))):
    LQ = 2 * detP / sp.sqrt(detg)
    print(nm, "EL of sqrt(g) Q:", EL(LQ, [u1, u2], t))
    Lvol = sp.sqrt(detg)
    print(nm, "EL of sqrt(g) (minimal surface check):", EL(Lvol, [u1, u2], t))
