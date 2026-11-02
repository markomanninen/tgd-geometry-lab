# Pointwise EL in physical signature, Moebius identifications, Lorentzian twistor examples, scaling of the non-Kaehler
# defect with a, refined quadrature, and the analytic prediction for dS_A.
from x6_kirjasto import *
from x6_a_testit import emb_A, emb_B
import numpy as np
rng = np.random.default_rng(3)
pts = [jnp.array(rng.normal(size=6)) * .6 for _ in range(4)]
def Yemb(fun):
    def f(x):
        ze, s, tau = fun(x)
        return jnp.concatenate([x, jnp.array([ze.real, ze.imag, s.real, s.imag, tau.real, tau.imag])])
    return f
eps = .8
wf = lambda x: c(x[2], x[3]); zf = lambda x: c(x[4], x[5])
tau_pre = lambda x: zf(x) * jnp.conj(-eps * wf(x)) / (1 + jnp.abs(eps * wf(x)) ** 2)
ex = {
 'hol s=eps w, tau=0': lambda x: (zf(x), eps * wf(x), 0j * zf(x)),
 'preimage tau=zeta d*/(1+|d|^2)': lambda x: (zf(x), eps * wf(x), tau_pre(x)),
 'hol Moebius zeta_F=2 zeta': lambda x: (2 * zf(x), eps * wf(x), 0j * zf(x)),
 'hol Moebius zeta_F=(zeta+.3w)/(1-.2 w zeta)': lambda x: ((zf(x) + .3 * wf(x)) / (1 - .2 * wf(x) * zf(x)), eps * wf(x), 0j * zf(x)),
 'hol s=eps w, tau=.5 zeta w': lambda x: (zf(x), eps * wf(x), .5 * zf(x) * wf(x)),
 'nonhol s=eps conj(w)': lambda x: (zf(x), eps * jnp.conj(wf(x)), 0j * zf(x)),
}
print('Physical signature G=du dv-|dw|^2+a dOmega^2-g_F(y=2): largest |H|, |E| over 4 points')
for nm, fu in ex.items():
    for a in (10., 1000.):
        Tf = lambda x: T_product(x, a, True)
        rs = [el(Yemb(fu), Tf, -1., 2., x, lam=.3) for x in pts]
        print(' %-46s a=%5.0f H %.3e  E %.3e' % (nm, a, max(float(r['H_size']) for r in rs), max(float(r['E_size']) for r in rs)), flush=True)
print('Lorentzian twistor functions Z1=w+zeta u, Z2=v+zeta conj(w) on product T')
for nm, em in (('s=eps Z1', emb_A(.8, True)), ):
    for a in (10., 1000.):
        Tf = lambda x: T_product(x, a, True)
        rs = [el(em, Tf, -1., 2., x, lam=.3) for x in pts]
        print(' %-20s a=%6.0f H %.3e E %.3e' % (nm, a, max(float(r['H_size']) for r in rs), max(float(r['E_size']) for r in rs)), flush=True)
def emb_BL(x):
    Z1, Z2 = Z12(x, True)
    return jnp.concatenate([x, jnp.array([x[4], x[5], eps * Z1.real, eps * Z1.imag, eps * Z2.real, eps * Z2.imag])])
for a in (10., 1000.):
    Tf = lambda x: T_product(x, a, True)
    rs = [el(emb_BL, Tf, -1., 2., x, lam=.3) for x in pts]
    print(' %-20s a=%6.0f H %.3e E %.3e' % ('s=eps Z1,tau=eps Z2', a, max(float(r['H_size']) for r in rs), max(float(r['E_size']) for r in rs)), flush=True)
print('Non-Kaehler defect, Euclidean target E4 x S2 with twistor J, surface B (b=-1), a scan')
pB = [p.at[:4].multiply(.2) for p in pts]
for a in (1e2, 1e3, 1e4, 1e5):
    Tf = lambda x: T_product(x, a, False)
    rs = [el(emb_B(.8), Tf, -1., 2., x) for x in pB]
    print(' a=%8.0f |H| %.4e  sqrt(a)|H| %.4f   a|H| %.4f  |E| %.4e' % (a, max(float(r['H_size']) for r in rs), np.sqrt(a) * max(float(r['H_size']) for r in rs), a * max(float(r['H_size']) for r in rs), max(float(r['E_size']) for r in rs)), flush=True)
# prediction for dS_A of the preimage: (4 pi b'^2 kappa^2/6) * (1/2) int d^2w sqrt(g) Q on the radial map
t, wt = np.polynomial.legendre.leggauss(400)
r1, r2m = .2, 1.2
rs_ = (r1 + r2m) / 2 + (r2m - r1) / 2 * t; wr = wt * (r2m - r1) / 2
def SQ(eta):
    tt = (rs_ - r1) / (r2m - r1); ch = (tt * (1 - tt)) ** 4 * 256
    dch = 4 * (tt * (1 - tt)) ** 3 * (1 - 2 * tt) * 256 / (r2m - r1)
    rt = eps * rs_ * (1 + eta * ch); drt = eps * (1 + eta * ch) + eps * rs_ * eta * dch
    A = drt / (1 + rt ** 2); B = rt / rs_ / (1 + rt ** 2)
    return 2 * np.pi / 3 * .5 * np.sum(wr * 2 * np.pi * rs_ * 2 * A ** 2 * B ** 2 / np.sqrt((1 + A ** 2) * (1 + B ** 2)))
print('prediction dS_Q/deta =', (SQ(1e-4) - SQ(-1e-4)) / 2e-4)
