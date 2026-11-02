# Holomorphic X6 (lam=0) against the preimage bundle (lam=1) over the same slice M2 x CP_1:
#   s = eps w (1+eta chi), d=-s, tau = lam * zeta conj(d)/(1+|d|^2).  G = du dv - |dw|^2 + a dOmega^2 + b g_F(y).
# Both have the slice zeta=0 equal. Table 1: fibre averages of R and |A|^2 against the two predictions.
# Table 2: first variation of S_vol, S_R, S_A under a radial bump chi(|w|^2) by Gauss quadrature.
from x6_kirjasto import *
import numpy as np, sys
LOR = True
def chi(r2, r1=.2, r2m=1.2):
    t = (jnp.sqrt(r2 + 1e-20) - r1) / (r2m - r1)
    return jnp.where((t > 0) & (t < 1), (t * (1 - t)) ** 4 * 256, 0.)
def family(eps, lam, eta):
    def zx(x):
        w = c(x[2], x[3]); ze = c(x[4], x[5]); r2 = x[2] ** 2 + x[3] ** 2
        s = eps * w * (1 + eta * chi(r2)); d = -s
        tau = lam * ze * jnp.conj(d) / (1 + jnp.real(d * jnp.conj(d)))
        return zxi_chart(ze, s, tau)
    return zx
def metric(a, b, y, eps, lam, eta):
    zx = family(eps, lam, eta)
    return lambda x: T_product(x, a, LOR) + b * pull_F(zx, x, y)
@jax.jit
def dens(x, a, b, y, eps, lam, eta):
    g = metric(a, b, y, eps, lam, eta)
    return jnp.array([sqrtdet(g, x), sqrtdet(g, x) * scal(g, x), sqrtdet(g, x) * A2(g, x)])
vd = jax.vmap(dens, in_axes=(0, None, None, None, None, None, None))
zs, ws = sph_grid(10, 8)   # U(1) invariance in phase of zeta and w: phi grid only as a check
def mk(xw):
    n = zs.shape[0]
    return jnp.concatenate([jnp.zeros((n, 2)), jnp.full((n, 1), xw), jnp.zeros((n, 1)), zs], axis=1)
def avg(a, b, y, eps, lam, xw):
    D = np.array(vd(mk(xw), a, b, y, eps, lam, 0.))
    wt = np.array(ws) * (1 + np.array(zs[:, 0]) ** 2 + np.array(zs[:, 1]) ** 2) ** 2 / 4
    v = np.sum(wt[:, None] * D, axis=0)
    return v  # integrals over d^2 zeta of sqrtG, sqrtG R, sqrtG |A|^2
y, eps, b = 2., .8, -1.
bp = b * y / 4
kap = 2.
print('Table 1. b=%g y=%g eps=%g, ints over fibre divided by fibre volume' % (b, y, eps))
for xw in (0.0, .5):
    f = eps ** 2 / (1 + eps ** 2 * xw ** 2) ** 2
    Q = 2 * f ** 2 / (1 + f) ** 2
    print(' |w|=%.2f Q=%.5f' % (xw, Q))
    for a in (10., 100., 1000., 10000.):
        rho2 = a + bp
        for lam in (0., 1.):
            v = avg(a, b, y, eps, lam, xw)
            print('  a=%7.0f lam=%g: vol/(4pi rho2) %.6f <R> %.6f  <R>rho2 %.5f  <A2> %.6e  <A2>/samecon %.4e  <A2>/flat %.5f' % (
                a, lam, v[0] / (4 * np.pi * rho2), v[1] / v[0], v[1] / v[0] * rho2, v[2] / v[0],
                v[2] / v[0] / (rho2 * kap ** 2 * Q / 6), v[2] / v[0] / (bp ** 2 / rho2 * kap ** 2 * Q / 6)), flush=True)
sys.stdout.flush()
# first variation: integrate over |w| in (r1,r2m) and over zeta
t, wt = np.polynomial.legendre.leggauss(14)
r1, r2m = .2, 1.2
rs = (r1 + r2m) / 2 + (r2m - r1) / 2 * t
wr = wt * (r2m - r1) / 2 * 2 * np.pi * rs
def S(a, b, y, eps, lam, eta):
    tot = np.zeros(3)
    wz = np.array(ws) * (1 + np.array(zs[:, 0]) ** 2 + np.array(zs[:, 1]) ** 2) ** 2 / 4
    for r, w_ in zip(rs, wr):
        tot += w_ * np.sum(wz[:, None] * np.array(vd(mk(r), a, b, y, eps, lam, eta)), axis=0)
    return tot
print('\nTable 2. dS/deta at 0 for S_vol, S_R, S_A, S_rest=S_R+S_A')
h = 1e-4
for lam in (0., 1.):
    for a in (10., 100., 1000.):
        dS = (S(a, b, y, eps, lam, h) - S(a, b, y, eps, lam, -h)) / (2 * h)
        print(' lam=%g a=%6.0f: dVol %.5e  dS_R %.5e  dS_A %.5e  dS_rest %.5e' % (lam, a, dS[0], dS[1], dS[2], dS[1] + dS[2]), flush=True)
