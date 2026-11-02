# Independent check: no autodiff, no frames. Example E (s=eps w, tau=0) is M2 x Y4 with Y4 Kaehler, potential
#  K = -w wb + 4 a log n2 - (log n2 + log(n2 + eps^2 w wb)), ds^2 = K_{i jb} dq dqb, R = -4 g^{i jb} d_i d_jb log det g.
# Exact rational values by sympy, then a plain mpmath finite difference of the hand formula for g_F on D.
import sympy as sp, mpmath as mp
w, wb, z, zb, a, e = sp.symbols('w wb z zb a e')
n2 = 1 + z * zb
K = -w * wb + 4 * a * sp.log(n2) - (sp.log(n2) + sp.log(n2 + e ** 2 * w * wb))
g = sp.Matrix([[sp.diff(K, w, wb), sp.diff(K, w, zb)], [sp.diff(K, z, wb), sp.diff(K, z, zb)]]).applyfunc(sp.together)
D = sp.factor(g.det())
LD = sp.log(D)
gi = g.inv().applyfunc(sp.together)
R = -4 * (gi[0, 0] * sp.diff(LD, w, wb) + gi[0, 1] * sp.diff(LD, z, wb) * 0 + gi[1, 0] * 0)
# g^{i jb}: g.inv() has entries [jb,i]; contract carefully
Ginv = g.inv()
R = 0
qs = [w, z]; qbs = [wb, zb]
for i in range(2):
    for j in range(2):
        R += Ginv[j, i] * sp.diff(LD, qs[i], qbs[j])
R = -4 * R
R = sp.together(R)
print('det g =', D)
vals = [(sp.Rational(1, 2), sp.Rational(1, 3), 5, sp.Rational(4, 5)), (sp.Rational(3, 7), sp.Rational(-2, 5), 100, sp.Rational(4, 5)), (0, 0, 10, sp.Rational(4, 5))]
for w0, z0, a0, e0 in vals:
    sub = {w: w0, wb: w0, z: z0, zb: z0, a: a0, e: e0}
    print('exact R(w=%s,z=%s,a=%s,e=%s) =' % (w0, z0, a0, e0), sp.nsimplify(sp.N(R.subs(sub), 25)) if False else sp.N(R.subs(sub), 16))
# exact expression at z=0 for general a, e, w
Rz0 = sp.factor(sp.together(R.subs({z: 0, zb: 0})))
print('R at zeta=0:', Rz0)
print('R at zeta=0, a->oo:', sp.factor(sp.limit(Rz0, a, sp.oo)))

# ---- mpmath finite differences of the hand formula, physical signature, same points
mp.mp.dps = 40
def gmat(x, A, eps, y=2):
    # x=(wr,wi,zr,zi); ds^2=-|dw|^2 + A dOmega^2 - [ |dz|^2 (|s|^2/(n^4 N^2)+ y/(n^2 N^2)) + |n^2 ds - zb s dz|^2/(n^2 N^4) ]
    wc = mp.mpc(x[0], x[1]); zc = mp.mpc(x[2], x[3]); s = eps * wc
    n = 1 + abs(zc) ** 2; N = n + abs(s) ** 2
    co = abs(s) ** 2 / (n ** 2 * N) + y / (n * N)
    # complex 1-forms in basis (dwr,dwi,dzr,dzi)
    dz = [0, 0, 1, mp.mpc(0, 1)]
    Ds = [n * eps, n * eps * mp.mpc(0, 1), -mp.conj(zc) * s, -mp.conj(zc) * s * mp.mpc(0, 1)]
    dw = [1, mp.mpc(0, 1), 0, 0]
    G = mp.matrix(4)
    for i in range(4):
        for j in range(4):
            G[i, j] = (-mp.re(dw[i] * mp.conj(dw[j])) + (4 * A / n ** 2 - co) * mp.re(dz[i] * mp.conj(dz[j]))
                       - mp.re(Ds[i] * mp.conj(Ds[j])) / (n * N ** 2))
    return G
def scal_fd(x0, A, eps, h=mp.mpf(10) ** (-10)):
    nd = 4
    G0 = gmat(x0, A, eps); Gi = G0 ** -1
    def shift(i, s, j=None, t=0):
        x = list(x0); x[i] += s * h
        if j is not None: x[j] += t * h
        return gmat(x, A, eps)
    d = [(shift(k, 1) - shift(k, -1)) / (2 * h) for k in range(nd)]
    dd = [[None] * nd for _ in range(nd)]
    for k in range(nd):
        for l in range(k, nd):
            dd[k][l] = dd[l][k] = (shift(k, 1, l, 1) - shift(k, 1, l, -1) - shift(k, -1, l, 1) + shift(k, -1, l, -1)) / (4 * h * h)
    # Christoffel low and derivative formula for R
    Gam = lambda l, i, j: sum(Gi[l, k] * (d[i][k, j] + d[j][k, i] - d[k][i, j]) for k in range(nd)) / 2
    GG = [[[Gam(l, i, j) for j in range(nd)] for i in range(nd)] for l in range(nd)]
    # dGi_k = -Gi dG Gi
    dGi = [-(Gi * d[k] * Gi) for k in range(nd)]
    def dGam(m, l, i, j):
        return sum(dGi[m][l, k] * (d[i][k, j] + d[j][k, i] - d[k][i, j]) + Gi[l, k] * (dd[m][i][k, j] + dd[m][j][k, i] - dd[m][k][i, j]) for k in range(nd)) / 2
    R_ = 0
    for i in range(nd):
        for j in range(nd):
            ric = sum(dGam(l, l, i, j) - dGam(j, l, i, l) for l in range(nd))
            ric += sum(GG[l][l][m] * GG[m][i][j] - GG[l][j][m] * GG[m][i][l] for l in range(nd) for m in range(nd))
            R_ += Gi[i, j] * ric
    return R_
for w0, z0, a0, e0 in [(.5, 1 / 3, 5, .8), (3 / 7, -.4, 100, .8), (0, 0, 10, .8)]:
    print('finite difference R', mp.nstr(scal_fd([mp.mpf(w0), mp.mpf('0'), mp.mpf(z0), mp.mpf('0')], mp.mpf(a0), mp.mpf(e0)), 14))
