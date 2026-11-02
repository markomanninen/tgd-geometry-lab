# Exact check of the reduced action for the ansatz
#   t, z, rho(s), psi = m*phi ; Theta(s), Phi = n*phi + omega*t + k*z
# Metric: ds^2 = dt^2 - dz^2 - N^2 ds^2 - p dphi^2 - W (n dphi + omega dt + k dz)^2
# with p = m^2 rho^2, W = a sin^2 Theta, signature (+,-,-,-).
# Claim:  sqrt|g| R = mu p' W'/(2 N P) + 2 (P'/N)',  P^2 = p(1-mu W) + n^2 W,  mu = omega^2-k^2.
# Riemann sign: R^a_bcd = d_c Gamma^a_bd - ..., R_bd = R^a_bad (so R=-2K on M2 x Y2).
import sympy as sp, random
from fractions import Fraction

s = sp.Symbol('s')
coords = sp.symbols('t z s phi')
idx_s = 2

def curvature(g):
    """Direct Christoffel -> Ricci -> scalar and Einstein tensor at s=0 (metric depends on s only)."""
    ginv = g.inv()
    dg = lambda a,b,c: sp.diff(g[a,b], coords[c])
    Gam = [[[sum(ginv[a,d]*(dg(d,c,b)+dg(d,b,c)-dg(b,c,d)) for d in range(4))/2
             for c in range(4)] for b in range(4)] for a in range(4)]
    Ric = sp.zeros(4,4)
    for b in range(4):
        for d in range(4):
            e = 0
            for a in range(4):
                e += sp.diff(Gam[a][b][d], coords[a]) - sp.diff(Gam[a][b][a], coords[d])
                for c in range(4):
                    e += Gam[a][a][c]*Gam[c][b][d] - Gam[a][d][c]*Gam[c][b][a]
            Ric[b,d] = e
    return ginv, Ric

def jet_test(seed):
    random.seed(seed)
    rnd = lambda : sp.Rational(random.randint(-9,9), random.randint(1,7))
    om, k, n = rnd(), rnd(), sp.Integer(random.choice([1,2,3]))
    p = sp.Integer(random.randint(1,5)) + rnd()*s + rnd()*s**2 + rnd()*s**3
    W = sp.Rational(1,random.randint(2,9)) + rnd()*s/10 + rnd()*s**2/10 + rnd()*s**3/10
    N = 1 + rnd()*s/10 + rnd()*s**2/10
    v = sp.Matrix([om, k, 0, n])
    eta = sp.diag(1, -1, -N**2, -p)
    g = eta - W*(v*v.T)
    ginv, Ric = curvature(g)
    Rs = sum(ginv[a,b]*Ric[a,b] for a in range(4) for b in range(4))
    mu = om**2 - k**2
    P2 = p*(1-mu*W) + n**2*W
    detg = sp.simplify(g.det())
    check_det = sp.simplify(detg + N**2*P2)
    P = sp.sqrt(P2)
    lhs = (N*P*Rs).subs(s,0)
    rhs = (mu*sp.diff(p,s)*sp.diff(W,s)/(2*N*P) + 2*sp.diff(sp.diff(P,s)/N,s)).subs(s,0)
    diff = sp.nsimplify(sp.simplify(lhs-rhs))
    return check_det, diff, complex(sp.N(lhs))

print("det g + N^2 P^2 and sqrt|g|R - formula on random exact jets:")
for seed in range(1,7):
    d, e, val = jet_test(seed)
    print(f" seed {seed}: det check {d}, residual {e}, sqrt|g|R = {val:.6f} (imaginary value means P^2<0 for this jet)")

# Symbolic derivation of Q = (tr A)^2 - tr A^2 = -2 mu p' W'/P^2
p0,W0,dp,dW,om,k,n = sp.symbols('p W dp dW omega k n')
v3 = sp.Matrix([om,k,n])
eta3 = sp.diag(1,-1,-p0)
G = eta3 - W0*v3*v3.T
Gd = sp.diag(0,0,-dp) - dW*v3*v3.T
A = G.inv()*Gd
Q = sp.simplify(A.trace()**2 - (A*A).trace())
mu = om**2-k**2
print("Q + 2 mu p' W'/P^2 =", sp.simplify(Q + 2*mu*dp*dW/(p0*(1-mu*W0)+n**2*W0)))
print("det G - P^2 =", sp.simplify(G.det()-(p0*(1-mu*W0)+n**2*W0)))
