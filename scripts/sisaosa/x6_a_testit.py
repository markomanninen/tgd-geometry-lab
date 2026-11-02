# Pipeline tests and the main type statement: R(F), R(CP3), holomorphy of the chart, EL=0 on Kaehler targets, EL!=0 on product+twistor J.
from x6_kirjasto import *
import numpy as np
rng = np.random.default_rng(1)
# 1. R(F)=24+8/y-2y
Fch = lambda q: zxi_chart(c(q[0], q[1]), c(q[2], q[3]), c(q[4], q[5]))
for y in (1., 2., 4., .7):
    g = lambda q: pull_F(Fch, q, y)
    q = jnp.array(rng.normal(size=6)) * .6
    print('R(F) y=%.1f numeric %.10f formula %.10f' % (y, scal(g, q), 24 + 8 / y - 2 * y))
# y=2 equals FS(z)+FS(xi)
q = jnp.array(rng.normal(size=6)) * .6
g2 = pull_F(Fch, q, 2.)
gs = fs(lambda q_: Fch(q_)[0], q) + fs(lambda q_: Fch(q_)[1], q)
print('y=2 minus FS(z)+FS(xi):', float(jnp.max(jnp.abs(g2 - gs))))
# 2. chart is complex for the (-,+,+) structure: metric Hermitian under standard J of the chart for every y
Jc = jnp.zeros((6, 6))
for i in range(3):
    Jc = Jc.at[2 * i, 2 * i + 1].set(-1).at[2 * i + 1, 2 * i].set(1)
for y in (1., 2.):
    gg = pull_F(Fch, q, y)
    print('Hermitian defect y=%.0f: %.2e' % (y, float(jnp.max(jnp.abs(Jc.T @ gg @ Jc - gg)))))
# base point of a twistor line: p fixed, zeta free
d, cc = .3 + .2j, -.4 + .1j
for ze in (.2 + .1j, -1 + .4j):
    s = ze * cc - d; tau = (ze * jnp.conj(d) + jnp.conj(cc)) / (1 + abs(d) ** 2 - ze * cc * jnp.conj(d))
    e1, e2, e3 = frames(*zxi_chart(ze, s, tau)); print('twistor line base', e3 / e3[0])
# 3. CP3: R=12/a
for a in (1., 3.):
    x = jnp.array(rng.normal(size=6)) * .5
    print('R(CP3) a=%g numeric %.8f formula %.8f' % (a, scal(lambda x_: T_cp3(x_, a), x), 12 / a))

# the examples. Euclidean, x=(Re a,Im a,Re b,Im b,Re zeta,Im zeta)
def emb_A(eps, lorentz=False):   # twistor J: s=eps Z1, tau=0
    def f(x):
        Z1, Z2 = Z12(x, lorentz)
        return jnp.concatenate([x, jnp.array([x[4], x[5], eps * Z1.real, eps * Z1.imag, 0., 0.])])
    return f
def emb_B(eps):                  # twistor J, rank 4 slices: s=eps Z1, tau=eps Z2
    def f(x):
        Z1, Z2 = Z12(x, False)
        return jnp.concatenate([x, jnp.array([x[4], x[5], eps * Z1.real, eps * Z1.imag, eps * Z2.real, eps * Z2.imag])])
    return f
def emb_E(eps):                  # product J: s=eps w (w=x2+i x3), tau=0
    def f(x):
        return jnp.concatenate([x, jnp.array([x[4], x[5], eps * x[2], eps * x[3], 0., 0.])])
    return f
if __name__ == '__main__':
    pts = [jnp.array(rng.normal(size=6)) * .7 for _ in range(4)]
    print('\n case: target, surface, a, b, y: largest |H|, largest |(Ein-Lam G)H| (Lam=0 and 0.7), tangential part of H')
    cases = [('CP3 x F, A', lambda a: (lambda x: T_cp3(x, a)), emb_A(.8), 2.),
             ('CP3 x F, B', lambda a: (lambda x: T_cp3(x, a)), emb_B(.8), 2.),
             ('prod J E4xS2 x F, E', lambda a: (lambda x: T_product(x, a, False)), emb_E(.8), 2.),
             ('prod+twistor J, A', lambda a: (lambda x: T_product(x, a, False)), emb_A(.8), 2.),
             ('prod+twistor J, B', lambda a: (lambda x: T_product(x, a, False)), emb_B(.8), 2.),
             ('CP3 x F(y=1), A', lambda a: (lambda x: T_cp3(x, a)), emb_A(.8), 1.)]
    for nm, Tf, em, y in cases:
        for a, b in ((3., 1.), (5., -1.), (100., -1.)):
            mx = [0, 0, 0, 0]
            for x in pts:
                r = el(em, Tf(a), b, y, x); r2 = el(em, Tf(a), b, y, x, lam=.7)
                mx = [max(mx[0], float(r['H_size'])), max(mx[1], float(r['E_size'])), max(mx[2], float(r2['E_size'])), max(mx[3], float(r['tang']))]
            print('%-24s a=%5.0f b=%2.0f y=%.0f  H %.3e  E0 %.3e  E.7 %.3e  tang %.1e' % (nm, a, b, y, *mx), flush=True)
