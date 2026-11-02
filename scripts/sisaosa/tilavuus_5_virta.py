# Exact stationary family in R x S2 x plane with finite flux through the signature change.
# Surface phi = w t + g(theta), L(p) = r sqrt|1 - w^2 r^2 S + S p^2|, p = g', S = sin^2 theta.
import sympy as sp, mpmath as mp

th = sp.Symbol('theta', positive=True)
t = sp.Symbol('t', real=True)
w, r, c = sp.symbols('omega r c', positive=True)
S = sp.sin(th)**2
pM2 = c**2*(1-w**2*r**2*S)/(S*(r**2*S-c**2))        # Minkowski side, A>0
pE2 = c**2*(w**2*r**2*S-1)/(S*(r**2*S+c**2))        # Euclidean side, A<0
AM = sp.simplify(1-w**2*r**2*S+S*pM2)
AE = sp.simplify(1-w**2*r**2*S+S*pE2)
print("A_M =", sp.factor(AM))
print("A_E =", sp.factor(AE))
print("check flux M: (r S p)^2/A - c^2 =", sp.simplify((r*S)**2*pM2/AM-c**2))
print("check flux E: (r S p)^2/|A| - c^2 =", sp.simplify((r*S)**2*pE2/(-AE)-c**2))

def surface_eq(p, sgn):
    # D_a d^a theta on the surface, using the 2x2 block in (t,theta)
    A = 1-w**2*r**2*S
    B = -r**2*w*S*p
    C = -r**2*(1+S*p**2)
    D = A*C-B**2
    sq = sp.sqrt(sgn*(-D))
    gtt, gtth, gthth = C/D, -B/D, A/D
    term1 = sp.diff(sq*gthth, th)/sq
    # Gamma^theta_{phi phi} = -sin cos with d_a phi = (w, p)
    gam = -sp.sin(th)*sp.cos(th)*(gtt*w**2+2*gtth*w*p+gthth*p**2)
    return term1+gam

P = sp.Function('P')(th)
vals = {w: sp.Rational(3, 1)/2, r: 1, c: sp.Rational(1, 5)}
ex = {}
for name, p2, sgn, thv, sign in (("Minkowski", pM2, 1, 0.5, 1), ("Euclidean", pE2, -1, 1.2, -1)):
    p = sign*sp.sqrt(p2.subs(vals))
    e = surface_eq(p, sgn).subs(vals)
    print(name, "D_a d^a theta at theta =", thv, ":", sp.N(e.subs(th, thv), 15))

w_, r_, c_ = 1.5, 1.0, 0.2
S0 = 1/(w_*r_)**2
th0 = mp.asin(mp.sqrt(S0))
print("theta0 =", th0, " turning point sin theta* = c/r:", mp.asin(c_/r_))
def fn(p2expr, A):
    return sp.lambdify(th, [p2expr.subs({w: w_, r: r_, c: c_}), A.subs({w: w_, r: r_, c: c_})], 'mpmath')
fM, fE = fn(pM2, AM), fn(pE2, AE)
print(" eps   p_M      A_M      c_M(flux phi)  j^th_t   |   p_E      A_E      c_E     j^th_t")
for eps in (1e-1, 1e-2, 1e-3, 1e-4, 1e-6):
    tm, te = th0-eps, th0+eps
    p2m, am = fM(tm); p2e, ae = fE(te)
    pm, pe = mp.sqrt(p2m), -mp.sqrt(p2e)
    Sm, Se = mp.sin(tm)**2, mp.sin(te)**2
    cm = r_*Sm*pm/mp.sqrt(am)
    ce = -r_*Se*pe/mp.sqrt(-ae)
    jtm = -r_*w_*Sm*pm/mp.sqrt(am)
    jte = r_*w_*Se*pe/mp.sqrt(-ae)
    print(eps, mp.nstr(pm, 5), mp.nstr(am, 5), mp.nstr(cm, 8), mp.nstr(jtm, 8), "|", mp.nstr(pe, 5), mp.nstr(ae, 5), mp.nstr(ce, 8), mp.nstr(jte, 8))

print()
print("slopes of A at theta0, left and right (det g4 has a kink):")
for e in (1e-5, 1e-7):
    print(e, mp.nstr(fM(th0-e)[1]/e, 8), mp.nstr(-fE(th0+e)[1]/e, 8))
print("ratio n_t/n_phi at X3 = -1/(r^2 S w) =", -1/(r_**2*S0*w_), " flux ratio j_t/j_phi = -omega =", -w_)

print()
print("Discrete gradient of S = sum L(p_i) d, node at theta0, grid spacing d")
def Lp(pv, thm):
    Sv = mp.sin(thm)**2
    A = 1-(w_*r_)**2*Sv+Sv*pv**2
    return (1 if A > 0 else -1)*r_*Sv*pv/mp.sqrt(abs(A))
for d in (1e-2, 1e-3, 1e-4):
    tm, te = th0-d/2, th0+d/2
    pm = mp.sqrt(fM(tm)[0]); pe = -mp.sqrt(fE(te)[0])
    print(d, "grad with sign flip p_E<0:", mp.nstr(Lp(pm, tm)-Lp(pe, te), 6),
          " grad with p_E>0:", mp.nstr(Lp(pm, tm)-Lp(-pe, te), 6))
