# (1) fibre metric of F over a fixed point p=(1:d:0): round in zeta for the unitary identification, Moebius image for zeta_F=zeta.
# (2) coefficient of |A|^2 for the preimage in the Kaehler target CP3 x F (Euclidean analogue of T(cd_conf)).
from x6_kirjasto import *
import numpy as np
d0 = .5 + .3j
def fib(mode):
    def zx(q):
        ze = c(q[0], q[1]); d = jnp.full_like(ze, d0); s = -d
        zF = ze * (jnp.sqrt(1 + abs(d0) ** 2) if mode == 2 else 1.)
        return zxi_chart(zF, s, zF * jnp.conj(d) / (1 + abs(d0) ** 2))
    return zx
for mode in (1, 2):
    for q in (jnp.array([.3, -.2]), jnp.array([1.1, .7])):
        g = pull_F(fib(mode), q, 2.)
        print('mode', mode, 'g_F on fibre / (y/4 dOmega^2) diag =', np.round(np.array(jnp.diag(g) / (.5 * jnp.diag(sphere(c(q[0], q[1]))))), 8), ' offdiag', float(g[0, 1]))
eps = .8
def fam(e, lam):
    def zx(x):
        w = c(x[2], x[3]); ze = c(x[4], x[5]); s = e * w; d = -s
        return zxi_chart(ze, s, lam * ze * jnp.conj(d) / (1 + jnp.real(d * jnp.conj(d))))
    return zx
zs, ws = sph_grid(10, 8)
wz = np.array(ws) * (1 + np.array(zs[:, 0]) ** 2 + np.array(zs[:, 1]) ** 2) ** 2 / 4
n = zs.shape[0]
X = jnp.concatenate([jnp.zeros((n, 4)), zs], axis=1)
print('CP3 x F, b=-1, y=2, w=0: rho^2 <|A|^2> and <R>')
for a in (1e2, 1e4):
    for e in (0., .8):
        for lam in (0., 1.):
            g = lambda x: T_cp3(x, a) - pull_F(fam(e, lam), x, 2.)
            f = jax.jit(lambda x: jnp.array([sqrtdet(g, x), sqrtdet(g, x) * scal(g, x), sqrtdet(g, x) * A2(g, x)]))
            D = np.array(jax.vmap(f)(X)); v = np.sum(wz[:, None] * D, axis=0)
            rho2 = a - .5
            print(' a=%6.0f eps=%.1f lam=%g rho2<A2> %.6f  rho2<R> %.5f' % (a, e, lam, rho2 * v[2] / v[0], rho2 * v[1] / v[0]), flush=True)
