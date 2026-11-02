#!/usr/bin/env python3
# Cosmic string tension: can Kahler-Chern-Simons give T = 1/(8 alpha_K R^2)?
# Conventions: metric on CP2 = R^2 * d d-bar log(1+|xi|^2) form, so that the
# geodesic length is pi R; dA = J, J is dimensionless, int_{CP1} J = pi.
# Run: uv run -q --no-project --with sympy python jannitys_lasku.py
import sympy as sp
from sympy import Rational as Q, pi, sin, cos, sqrt, symbols, Function, Matrix, simplify, integrate

R, alpha, G, Lam = symbols('R alpha_K G Lambda', positive=True)
k1 = 1/(16*pi*alpha)
Tpub = 1/(8*alpha*R**2)

print("=== A. Normalisation from the full CP2")
x1, y1, x2, y2 = X = symbols('x1 y1 x2 y2', real=True)
K = sp.log(1 + x1**2 + y1**2 + x2**2 + y2**2)
z = [(x1, y1), (x2, y2)]
def dzbz(f, a, b):
    # d/dz_a d/dzbar_b f
    d = lambda g, c: (sp.diff(g, z[c][0]) - sp.I*sp.diff(g, z[c][1]))/2
    db = lambda g, c: (sp.diff(g, z[c][0]) + sp.I*sp.diff(g, z[c][1]))/2
    return d(db(f, b), a)
h = Matrix(2, 2, lambda a, b: dzbz(K, a, b))
# real metric (R=1) ds^2 = h_ab dz^a dzbar^b, Kahler form J with J = vol on CP1
pt = {x1: Q(1, 3), y1: Q(2, 5), x2: Q(-1, 2), y2: Q(1, 7)}
h0 = h.subs(pt).applyfunc(sp.nsimplify)
g = sp.zeros(4)
for a in range(2):
    for b in range(2):
        Hab = h0[a, b]; re, im = sp.re(Hab), sp.im(Hab)
        i, j = 2*a, 2*b
        # h = S + iW gives ds^2 = dx S dx + dy S dy + 2 dx W dy
        g[i, j] += re; g[i+1, j+1] += re; g[i, j+1] += im; g[i+1, j] -= im
g = g.applyfunc(simplify)
# complex structure I d/dx = d/dy, I d/dy = -d/dx; J_ij = g(I e_i, e_j)
Ic = sp.zeros(4)
for a in range(2):
    Ic[2*a+1, 2*a] = 1; Ic[2*a, 2*a+1] = -1
Jm = (Ic.T*g).applyfunc(simplify)
print(" J antisymmetric:", (Jm + Jm.T).applyfunc(simplify) == sp.zeros(4))
ginv = g.inv()
JJ = simplify(sum(Jm[i, j]*(ginv*Jm*ginv.T)[i, j] for i in range(4) for j in range(4)))
print(" J_kl J^kl on CP2 at a generic point (R=1):", JJ)
print(" book value L = 4/R^4 (tgdclass1.txt line 5925-5938)")
th, ph = symbols('theta phi', positive=True)
area = integrate(integrate(sin(th)/4, (th, 0, pi)), (ph, 0, 2*pi))
print(" CP1 metric (R^2/4)(dth^2+sin^2 th dph^2), area/R^2 =", area)
JthPh = sin(th)/4                 # J = vol/R^2 in dimensionless form
flux = integrate(integrate(JthPh, (th, 0, pi)), (ph, 0, 2*pi))
print(" flux int_{CP1} J =", flux)
# on CP1 the frame component of J is j = 1/R^2, so J_ab J^ab = 2 j^2 = 2/R^4
T_K = k1*(2/R**4)*(pi*R**2)
print(" T_K = k1 * J_ab J^ab * area =", simplify(T_K), " equal to published:", simplify(T_K - Tpub) == 0)
S_CP2 = k1*(4/R**4)*(pi**2*R**4/2)
print(" S_K(CP2) = k1 * 4/R^4 * V =", simplify(S_CP2), " (book pi/(8 alpha_K))")
print(" identity T * area(CP1) - S_K(CP2) =", simplify(Tpub*pi*R**2 - S_CP2))
print(" structure: T = 2 k1 Phi^2 / Area with Phi = pi:", simplify(2*k1*flux**2/(pi*R**2) - Tpub))
print(" scaling under R -> lam R: T ~ lam^-2 (Hodge star), K-C-S ~ lam^0 (no metric)")

print("\n=== B. No degenerate metric on the string")
t, zz = symbols('t z', real=True)
gs = sp.diag(1, -1, -R**2/4, -R**2*sin(th)**2/4)
print(" det g =", simplify(gs.det()), " nonzero away from the coordinate poles")

print("\n=== C. A^J vanishes on every 3-surface inside M^2 x CP1")
a1, a2, a3 = coords = symbols('a1 a2 a3', real=True)
tf, zf, thf, phf = [Function(n)(a1, a2, a3) for n in ('t', 'z', 'th', 'ph')]
c, c1, c2 = symbols('c c1 c2', real=True)
# Generic potential on CP1 in any CP2 gauge: A = P(th,ph) dth + Q(th,ph) dph
Pf, Qf = Function('P'), Function('Q')
Ath, Aph = Pf(thf, phf), Qf(thf, phf)
Jtp = sp.diff(Qf(th, ph), th) - sp.diff(Pf(th, ph), ph)
Jtp_on = Function('Jtp')(thf, phf)
Aa = [Ath*sp.diff(thf, a) + Aph*sp.diff(phf, a) for a in coords]
Jab = lambda a, b: Jtp_on*(sp.diff(thf, a)*sp.diff(phf, b) - sp.diff(phf, a)*sp.diff(thf, b))
dens = 0
for (p, q, r), sgn in [((0, 1, 2), 1), ((1, 2, 0), 1), ((2, 0, 1), 1), ((0, 2, 1), -1), ((2, 1, 0), -1), ((1, 0, 2), -1)]:
    dens += sgn*Aa[p]*Jab(coords[q], coords[r])
print(" epsilon^abc A_a J_bc on a general 3-surface =", simplify(sp.expand(dens)))

print("\n=== D. Canonical momentum of the CP2 K-C-S in M4 directions")
print(" L_KCS(CP2) contains no M4 coordinate, so Pi^alpha_{m^k} = 0 identically and the")
print(" action is linear in time derivatives, hence its Hamiltonian is zero.")

print("\n=== E. Hodge star: the Kahler action on the string as a boundary term")
# *J pulled to M^2 is dt^dz/R^2 (dimension 1/length^2), J pulled to CP1 is J
L_str, tau = symbols('L tau', positive=True)
S_bulk = k1*(2/R**4)*(pi*R**2)*L_str*tau
# 2 k1 J ^ *J = 2 k1 d(A ^ *J); the only surviving boundary is the Dirac sheet
# M^2 x equator-type circle, where the jump of A integrates to the flux pi.
S_dirac = 2*k1*(L_str*tau/R**2)*pi
print(" bulk action, Dirac-sheet boundary form, difference:", simplify(S_bulk), simplify(S_dirac), simplify(S_bulk - S_dirac))
print(" pullback of *J to L x CP1 (z=const) is 0, pullback of J is not, so *J = kappa J fails")
print(" CP2-type extremal: *J = J, 2 k1 int J^J = 2 k1 pi^2 =", simplify(2*k1*pi**2), "= S_K(CP2)")

print("\n=== F. End energy with a time component B_t = c (option a cross term)")
kF = symbols('k_F', positive=True)   # S_CS = k_F int A ^ J; k_F = 2 k_eps when L = k_eps eps A J
E_end = kF*pi*c
print(" S on (t in tau) x CP1 = k_F * c * tau * pi, so E_end =", E_end)
ell = sp.solve(E_end/symbols('ell', positive=True) - Tpub, symbols('ell', positive=True))
print(" length ell with E_end = T*ell:", simplify(ell[0]))
for name, kv in [("k_F=k1", k1), ("k_F=2k1 (k1 eps A J)", 2*k1), ("k_F=4k1 (Martin1 1/(2g^2) eps A J)", 4*k1)]:
    print("  ", name, ": ell/(c R^2) =", simplify((kv*pi*c/Tpub)/(c*R**2)), ", E_end at c=1/R:", simplify(kv*pi/R))
# Check of the Noether current normalisation for constant phi
print(" direct: Pi^t_t integrated over CP1 for L = eps A J:", 2*c*pi, " versus -4 phi Phi with phi=-c:", 4*c*pi)
print(" the difference is the patch term from d(phi A) on CP1, nonzero because A is not global")
# Linear potential: Delta B_t = c_M L between the ends
cM = symbols('c_M', positive=True)
print(" linear case: E = k_F pi c_M L, so T = k_F pi c_M; c_M needed for T_pub:", simplify(Tpub/(kF*pi)))
print("   for k_F=k1:", simplify(Tpub/(k1*pi)), " for k_F=2k1:", simplify(Tpub/(2*k1*pi)), " for k_F=4k1:", simplify(Tpub/(4*k1*pi)))

print("\n=== G. Exact J(M4) gives zero flux on a closed partonic surface")
u, v = symbols('u v', real=True)
X_, Y_ = Function('X')(u, v), Function('Y')(u, v)
# J^M = dx^dy = d(x dy): on a closed surface the integral is a boundary term
JM = sp.diff(X_, u)*sp.diff(Y_, v) - sp.diff(X_, v)*sp.diff(Y_, u)
dv = sp.diff(X_*sp.diff(Y_, v), u) - sp.diff(X_*sp.diff(Y_, u), v)
print(" pullback(J^M) - d(x dy) =", simplify(JM - dv))
print(" so int_{closed X^2} J^M = 0 when J^M = dx^dy is global on M4")

print("\n=== H. R + volume on M^2 x Y^2")
gT = {}
cV, cR = symbols('c_V c_R')
Sarea, chi = symbols('S chi')
Tgen = cV*Sarea - 4*pi*chi*cR
print(" general T =", Tgen)
print(" c_V=Lam/(8 pi G), c_R=1/(16 pi G):", simplify(Tgen.subs({cV: Lam/(8*pi*G), cR: 1/(16*pi*G)})*8*G))
d = symbols('d', positive=True, integer=True)
print(" degree d holomorphic curve: 8GT =", sp.factor(simplify((Tgen.subs({cV: Lam/(8*pi*G), cR: 1/(16*pi*G)})*8*G).subs({Sarea: d*pi*R**2, chi: 3*d-d**2}))))
RG = sp.Float('7.8e7')
aK = Q(1, 137)
eightGT = (1/(aK*RG)).evalf()
print(" 8 G T_pub = G/(alpha_K R^2) with R^2/G=7.8e7:", eightGT)
print(" check R^2/G from G T=0.22e-6:", (1/(8*aK*sp.Float('0.22e-6'))).evalf())
for lab, fac, shift in [("d=1 R+V", 1, -4), ("d=1 V only", 1, 0), ("d=2 R+V", 2, -4), ("d=3 torus", 3, 0), ("d=2 V only", 2, 0)]:
    print("  ", lab, ": Lam R^2 =", (eightGT - shift)/fac)
# Clifford torus, unit S^5 horizontal metric, geodesic length pi
vol_cliff = 4*pi**2/(3*sqrt(3))
print(" Clifford torus area/R^2 =", vol_cliff, vol_cliff.evalf(), ", 8GT/(Lam R^2) =", simplify(vol_cliff/pi), (vol_cliff/pi).evalf())
print("   Lam R^2 for T_pub:", (eightGT/(vol_cliff/pi)).evalf())
print(" Lam needed in terms of Gaussian curvature: K(CP1)=4/R^2, so Lam R^2=4 is Lam=K")
print(" twistor lift, hgrtwistor eq 2.3 with Area/S0=1: rho_vac = 2/(alpha_K R1^4)")
R1 = symbols('R_1', positive=True)
sol = sp.solve(2/(alpha*R1**4)*pi*R**2 - Tpub, R1)
print("  rho_vac * pi R^2 = T_pub gives R1 =", sol, [s.evalf() / R for s in sol])
print(" tolerance: |Lam R^2 - 4| must be below about", eightGT, " for |T| of the published size")
print(" lightest density of contacts: CP2 instanton per M^2 area a: a = S_K(CP2)/T =", simplify(S_CP2/Tpub))
print(" Fermion unit count if the end charge were 1/(4 alpha_K):", 137/4)
