# Exact pure-volume models with a det g4 = 0 surface: charges, flux, K-C-S.
import sympy as sp
import numpy as np

print("=== Model A: rotating rod x CP1, X4 = Y2 x CP1, Y2: phi = k t in M4 ===")
t, rho, th, ph = sp.symbols('t rho theta phi', real=True)
k, Rr = sp.symbols('k R', positive=True)
q = (t, rho, th, ph)
x = rho*sp.cos(k*t); y = rho*sp.sin(k*t)
m4 = [t, x, y, sp.Integer(0)]
eta = sp.diag(1, -1, -1, -1)
s = sp.diag(Rr**2/4, Rr**2/4*sp.sin(th)**2)      # CP1 of area pi R^2, from jannitys.md

def metric(map4, cp):
    g = sp.zeros(4, 4)
    for a in range(4):
        for b in range(4):
            g[a, b] = sum(eta[i, i]*sp.diff(map4[i], q[a])*sp.diff(map4[i], q[b]) for i in range(4)) \
                - sum(s[i, i]*sp.diff(cp[i], q[a])*sp.diff(cp[i], q[b]) for i in range(2))
    return sp.simplify(g)

g = metric(m4, [th, ph])
print("g =", g.tolist())
detg = sp.simplify(g.det())
print("det g =", sp.factor(detg))
ginv = g.inv().applyfunc(sp.simplify)
# region k rho < 1 : sqrt|g| = sqrt(1-k^2 rho^2) * R^2 sin th/4
Dm = 1 - k**2*rho**2
sq = sp.sqrt(Dm)*Rr**2*sp.sin(th)/4
for name, fn in (("t", t), ("x", x), ("y", y)):
    e = sum(sp.diff(sq*sum(ginv[a, b]*sp.diff(fn, q[b]) for b in range(4)), q[a]) for a in range(4))
    print("div j(", name, ") =", sp.simplify(e))

print("normal currents j^rho_k: sqrt|g| g^{rho rho} d_rho m_k ->", sp.simplify(sq*ginv[1, 1]*sp.diff(x, rho)), " -> 0 at k rho=1 as sqrt(1-k^2 rho^2)")
jt = sq*ginv[0, 0]
print("energy density per unit CP1 element:", sp.simplify(jt/(Rr**2*sp.sin(th)/4)))
T = sp.Symbol('T', positive=True)
E = sp.integrate(T/sp.sqrt(1-k**2*rho**2), (rho, -1/k, 1/k))
L = sp.integrate(T*k*rho**2/sp.sqrt(1-k**2*rho**2), (rho, -1/k, 1/k))
print("E =", sp.simplify(E), " L =", sp.simplify(L), " E^2/(2 pi T L) =", sp.simplify(E**2/(2*sp.pi*T*L)))
print("T = c_V * pi R^2 is the volume tension of the CP1 factor.")

print()
print("--- fold chart (tau,sigma): x+iy = (1/k) cos(k sigma) e^{i k tau} ---")
tau, sig = sp.symbols('tau sigma', real=True)
X = sp.cos(k*sig)*sp.cos(k*tau)/k; Y = sp.cos(k*sig)*sp.sin(k*tau)/k
gtt = sp.simplify(1 - sp.diff(X, tau)**2 - sp.diff(Y, tau)**2)
gss = sp.simplify(-sp.diff(X, sig)**2 - sp.diff(Y, sig)**2)
gts = sp.simplify(-sp.diff(X, tau)*sp.diff(X, sig) - sp.diff(Y, tau)*sp.diff(Y, sig))
print("g_tautau =", gtt, " g_sigsig =", gss, " g_tausig =", gts)
print("sqrt|g2| g^{sigma sigma} =", sp.simplify(sp.Abs(gtt)/gss if False else -1), "(constant), and d_sigma h -> 0 at sigma=0:",
      sp.simplify(sp.diff(X, sig).subs(sig, 0)))
u, v_ = sp.symbols('u v', real=True)
W = (sp.exp(sp.I*k*u)+sp.exp(sp.I*k*v_))/(2*k)
print("with u=tau+sigma, v=tau-sigma: x+iy =", W, "; both u and v appear; d_u d_v W =", sp.diff(W, u, v_))
print("X3 is sigma=0 which is u=v, not a level set of u or v.")

print()
print("--- Euclidean continuation rho>1/k, sign of the energy density with sqrt|g| ---")
rr = sp.Symbol('r', positive=True)  # r = k rho > 1
print("j^t_t/T = sqrt(r^2-1)/(1-r^2) =", sp.simplify(sp.sqrt(rr**2-1)/(1-rr**2)), " negative")

print()
print("--- K-C-S on X3 = {rho=1/k} x CP1, in chart (t,theta,phi) ---")
J12 = Rr**0*sp.sin(th)/2    # J = (1/2) sin th dth^dphi gives flux 2 pi? normalised below
print("flux check, int J over CP1 with J = (1/4)... ; repo value is pi, use J=(1/4) sin th dth^dphi:",
      sp.integrate(sp.Rational(1, 4)*sp.sin(th), (th, 0, sp.pi))*2*sp.pi)
print("n^alpha = (2 J_thph, 0, 0), V = 2 J_thph d_t h, V_C = 0 because theta,phi do not depend on t")
print("E^C = 0. A^C has no t component so A^C ^ J^C = 0 pointwise, density zero, charge Q_A = -4 int phi_A J != 0")
print("n = d_t h = (1, -k y, k x, 0) has null M4 part:", sp.simplify((1-sp.diff(x, t)**2-sp.diff(y, t)**2).subs(rho, 1/k)))
acc = [sp.diff(sp.diff(x, t), t).subs(rho, 1/k), sp.diff(sp.diff(y, t), t).subs(rho, 1/k)]
print("generator acceleration:", [sp.simplify(a) for a in acc], " norm k: not a geodesic of H")

print()
print("=== Model B: warped rod, Y2 in R x S2, phi = w t, times plane (y,z) ===")
w, r = sp.symbols('omega r', positive=True)
q2 = (t, th)
gtt2 = 1 - w**2*r**2*sp.sin(th)**2
print("g_tt =", gtt2, " g_thth = -r^2, X3 at sin th0 = 1/(w r)")
# check field equation of phi: d_a( sqrt|g| g^{ab} d_b phi ) = 0 and t: same, static in t
sq2 = sp.sqrt(gtt2)*r
print("div j(phi) = d_t( sqrt|g| g^tt w ) + d_th(0) =", sp.diff(sq2/gtt2*w, t))
# covariant form: D_a j^a_theta = (1/sqrt|g|) d_a(sqrt|g| g^{ab} d_b theta) + Gamma^theta_{phi phi} g^{tt} w^2
Gam = -sp.sin(th)*sp.cos(th)
cov = sp.diff(sq2*(-1/r**2), th)/sq2 + Gam*w**2/gtt2
print("D_a D^a theta =", sp.simplify(cov))
print("n = d_t + w d_phi, n_M = (1,0,0,0) timelike, n_C = w d_phi != 0; J^C pullback to X3 vanishes because theta is constant there.")

import mpmath as mp
print()
print("wr   theta0   E/(c_V r A2)  charge_phi/(c_V r^2 A2), one fold between theta0 and pi-theta0 around the POLE side (Minkowski region)")
for wr in (1.1, 1.5, 2.0, 5.0):
    th0 = mp.asin(1/mp.mpf(wr))
    # Minkowski region is sin th < 1/(w r), around the poles
    E_ = mp.quad(lambda a: 1/mp.sqrt(1-wr**2*mp.sin(a)**2), [0, th0])
    L_ = mp.quad(lambda a: mp.sin(a)**2*wr/mp.sqrt(1-wr**2*mp.sin(a)**2), [0, th0])
    print(wr, mp.nstr(th0, 6), mp.nstr(mp.re(2*E_), 8), mp.nstr(mp.re(2*L_), 8))
