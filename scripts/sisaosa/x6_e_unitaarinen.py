# Preimage with the isometric (unitary radial frame) identification zeta_F = zeta sqrt(1+|d|^2), refined quadrature for the
# holomorphic case, and comparison of the autodiff R with the exact values of x6_c.
from x6_kirjasto import *
import numpy as np
def chi(r2, r1=.2, r2m=1.2):
    t = (jnp.sqrt(r2 + 1e-20) - r1) / (r2m - r1)
    return jnp.where((t > 0) & (t < 1), (t * (1 - t)) ** 4 * 256, 0.)
def family(eps, mode, eta):
    def zx(x):
        w = c(x[2], x[3]); ze = c(x[4], x[5]); r2 = x[2] ** 2 + x[3] ** 2
        s = eps * w * (1 + eta * chi(r2)); d = -s
        if mode == 0:   # holomorphic
            return zxi_chart(ze, s, 0j * ze)
        if mode == 1:   # preimage, holomorphic frame
            return zxi_chart(ze, s, ze * jnp.conj(d) / (1 + jnp.real(d * jnp.conj(d))))
        zF = ze * jnp.sqrt(1 + jnp.real(d * jnp.conj(d)))   # preimage, unitary frame
        return zxi_chart(zF, s, zF * jnp.conj(d) / (1 + jnp.real(d * jnp.conj(d))))
    return zx
def metric(a, b, y, eps, mode, eta):
    zx = family(eps, mode, eta)
    return lambda x: T_product(x, a, True) + b * pull_F(zx, x, y)
from functools import partial
@partial(jax.jit, static_argnames=('mode',))
def dens(x, a, b, y, eps, mode, eta):
    g = metric(a, b, y, eps, mode, eta)
    return jnp.array([sqrtdet(g, x), sqrtdet(g, x) * scal(g, x), sqrtdet(g, x) * A2(g, x)])
def vd(X, a, b, y, eps, mode, eta):
    return jax.vmap(lambda x: dens(x, a, b, y, eps, mode, eta))(X)
# exact comparison
for (w0, z0, a0, ex) in ((.5, 1 / 3, 5., -0.05869489161039816), (3 / 7, -.4, 100., -0.6482824241123804), (0., 0., 10., -0.9256395002974420)):
    g = metric(a0, -1., 2., .8, 0, 0.)
    print('autodiff R %.13f  exact %.13f' % (scal(g, jnp.array([.1, .2, w0, 0., z0, 0.])), ex))
y, eps, b = 2., .8, -1.
bp = b * y / 4; kap = 2.
for nth in (10,):
    zs, ws = sph_grid(nth, 4)
    wz = np.array(ws) * (1 + np.array(zs[:, 0]) ** 2 + np.array(zs[:, 1]) ** 2) ** 2 / 4
    def mk(xw):
        n = zs.shape[0]
        return jnp.concatenate([jnp.zeros((n, 2)), jnp.full((n, 1), xw), jnp.zeros((n, 1)), zs], axis=1)
    nr = 14 if nth == 10 else 28
    t, wt = np.polynomial.legendre.leggauss(nr)
    r1, r2m = .2, 1.2
    rs = (r1 + r2m) / 2 + (r2m - r1) / 2 * t; wr = wt * (r2m - r1) / 2 * 2 * np.pi * rs
    def S(a, mode, eta):
        tot = np.zeros(3)
        for r, w_ in zip(rs, wr):
            tot += w_ * np.sum(wz[:, None] * np.array(vd(mk(float(r)), a, b, y, eps, mode, eta)), axis=0)
        return tot
    h = 1e-4
    print('nth', nth, 'nr', nr)
    for mode in (0, 1, 2):
        for a in (100., 10000.):
            dS = (S(a, mode, h) - S(a, mode, -h)) / (2 * h)
            print(' mode=%d a=%7.0f dVol %.4e dS_R %.6e dS_A %.6e sum %.4e' % (mode, a, dS[0], dS[1], dS[2], dS[1] + dS[2]), flush=True)
    if nth == 10:
        for xw in (.5, 1.):
            f = eps ** 2 / (1 + eps ** 2 * xw ** 2) ** 2; Q = 2 * f ** 2 / (1 + f) ** 2
            for mode in (0, 1, 2):
                for a in (100., 10000.):
                    rho2 = a + bp
                    v = np.sum(wz[:, None] * np.array(vd(mk(xw), a, b, y, eps, mode, 0.)), axis=0)
                    print(' |w|=%.1f mode=%d a=%7.0f vol/(4pi rho2) %.6f sqrt(g4)=2*that, 1+f=%.6f <R> %.6f <A2>/flat %.5f' % (xw, mode, a, v[0] / (4 * np.pi * rho2), 1 + f, v[1] / v[0], v[2] / v[0] / (bp ** 2 / rho2 * kap ** 2 * Q / 6)), flush=True)
