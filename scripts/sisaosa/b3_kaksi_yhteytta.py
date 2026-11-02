# Direct Ricci scalar of the 4D model S^2_b x S^2_f with rational coordinates
# x = cos(theta), w = cos(vartheta), which keeps every entry rational.
import sympy as sp

x, ph, w, vp = sp.symbols("x phi w varphi")
B2, q, a, b, h, e = sp.symbols("B2 q a b h e", nonzero=True)
X = [x, ph, w, vp]
c = lambda v: sp.cancel(sp.together(v))


def scalar_curvature(g):
    n = 4
    gi = g.inv().applyfunc(c)
    Gam = [[[c(sum(gi[i, d] * (sp.diff(g[d, j], X[k]) + sp.diff(g[d, k], X[j]) - sp.diff(g[j, k], X[d]))
                   for d in range(n)) / 2) for k in range(n)] for j in range(n)] for i in range(n)]
    tot = 0
    for j in range(n):
        for k in range(n):
            if gi[j, k] == 0:
                continue
            v = 0
            for i in range(n):
                v += sp.diff(Gam[i][j][k], X[i]) - sp.diff(Gam[i][j][i], X[k])
                for d in range(n):
                    v += Gam[i][i][d] * Gam[d][j][k] - Gam[i][k][d] * Gam[d][j][i]
            tot += gi[j, k] * c(v)
    return c(tot)


def metric(base, fa, fb, A):
    # base*(dx^2/(1-x^2)+(1-x^2)dphi^2) + fa*dOmega + fb*(dw^2/(1-w^2)+(1-w^2)(dvp+A dphi)^2)
    g = sp.zeros(4)
    g[0, 0] = base / (1 - x**2)
    g[1, 1] = base * (1 - x**2) + fb * (1 - w**2) * A**2
    g[1, 3] = g[3, 1] = fb * (1 - w**2) * A
    g[2, 2] = (fa + fb) / (1 - w**2)
    g[3, 3] = (fa + fb) * (1 - w**2)
    return g



A = (1 - x)
Rr = sp.Rational
for (av, bv, ev, qv) in ((9, -1, -1, 1), (4, -1, -1, 1), (100, -1, -1, 1), (0, -1, -1, 1)):
    R = scalar_curvature(metric(ev * 1, av, bv, qv * A))
    print("a,b,e,q =", av, bv, ev, qv, flush=True)
    print(" R =", sp.factor(R), flush=True)
    print(" R(x=1) =", sp.factor(R.subs(x, 1)), flush=True)
    print(" R(x=-1) =", sp.factor(R.subs(x, -1)), flush=True)
