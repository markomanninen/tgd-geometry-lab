# Pointwise algebra of the K-C-S force against a null jump lambda*n_k, exact rationals.
# H tangent space: M4 (t,x,y,z) with metric diag(1,-1,-1,-1) plus CP2 with -delta in the H metric.
import sympy as sp, random, itertools
R = sp.Rational
random.seed(7)

m = sp.diag(1, -1, -1, -1)
h = sp.diag(1, -1, -1, -1, -1, -1, -1, -1)          # H metric, signature (1,7)
I4 = sp.Matrix([[0, 1, 0, 0], [-1, 0, 0, 0], [0, 0, 0, 1], [0, 0, -1, 0]])   # J(CP2) at a point

def Jblock(M=None, C=None):
    J = sp.zeros(8, 8)
    if M is not None:
        J[:4, :4] = M
    if C is not None:
        J[4:, 4:] = C
    return J

Jm_tr = sp.zeros(4, 4); Jm_tr[1, 2] = 1; Jm_tr[2, 1] = -1          # dx^dy, kernel (t,z)
Jm_fu = Jm_tr.copy();   Jm_fu[0, 3] = 1; Jm_fu[3, 0] = -1          # dt^dz + dx^dy

def pull(J, T):
    return T.T*J*T

def Vof(J, T):
    P = pull(J, T)
    na = sp.Matrix([2*P[1, 2], 2*P[2, 0], 2*P[0, 1]])                 # eps^{abc} J_bc
    return T*na, P, na

def E(J, T):
    # E_k = 2 J_kl V^l with V built from the same J
    V, P, na = Vof(J, T)
    return 2*J*V

def rnd(n=8):
    return sp.Matrix([R(random.randint(-9, 9), random.randint(1, 5)) for _ in range(n)])

def tangent_orth(n):
    # random e with h(n,e)=0
    e = rnd()
    hn = h*n
    idx = max(range(8), key=lambda i: abs(hn[i]))
    e[idx] = 0
    e[idx] = -(hn.T*e)[0]/hn[idx]
    return e

# warped null generator: n_M timelike, n_C nonzero
n_warp = sp.Matrix([5, 3, 0, 0, 4, 0, 0, 0])
# unwarped null generator in M4
n_null = sp.Matrix([1, 0, 0, 1, 0, 0, 0, 0])
for nn in (n_warp, n_null):
    assert (nn.T*h*nn)[0] == 0

print("=== 1. Identities on random frames ===")
for trial in range(3):
    n = n_warp
    T = sp.Matrix.hstack(n, tangent_orth(n), tangent_orth(n))
    Ja = Jblock(Jm_fu, I4)
    Ea = E(Ja, T)
    JM = Jblock(Jm_fu, None); JC = Jblock(None, I4)
    EM = E(JM, T); EC = E(JC, T)
    print("trial", trial,
          "E_a.t =", list((Ea.T*T)), "EM.t =", list((EM.T*T)), "EC.t =", list((EC.T*T)))

print()
print("=== 2. Warped generator: can lambda n_k + cM EM + cC EC vanish with lambda != 0? ===")
def nlow(n):
    return h*n

def solve(n, JM, JC, option, tries=4, transversal=False):
    res = []
    for _ in range(tries):
        e1, e2 = tangent_orth(n), tangent_orth(n)
        if transversal:
            # impose J(n,e_i)=0 for the total J by fixing one more coefficient
            J = JM + JC
            for e in (e1, e2):
                w = J.T*n
                # keep h(n,e)=0: solve in the 2-plane spanned by two h-orthogonal vectors
                p, q = tangent_orth(n), tangent_orth(n)
                a_, b_ = sp.symbols('a_ b_')
                ee = e + a_*p + b_*q
                s = sp.solve([(n.T*J*ee)[0]], [a_], dict=True)
                if s:
                    e[:, 0] = ee.subs(s[0]).subs(b_, 0)
        T = sp.Matrix.hstack(n, e1, e2)
        if option == 'a':
            J = JM + JC
            A = sp.Matrix.hstack(nlow(n), E(J, T))
        else:
            A = sp.Matrix.hstack(nlow(n), E(JM, T), E(JC, T))
        ns = A.nullspace()
        lamfree = any(v[0] != 0 for v in ns)
        res.append(("rank", A.rank(), "cols", A.shape[1], "lambda!=0 possible", lamfree))
    return res

JMt = Jblock(Jm_tr, None); JMf = Jblock(Jm_fu, None); JC = Jblock(None, I4)
for label, n in (("warped", n_warp), ("unwarped", n_null)):
    for jlabel, JM in (("J(M4) transversal", JMt), ("J(M4) full", JMf)):
        for opt in ('a', 'b'):
            r = solve(n, JM, JC, opt)
            print(f"{label:9s} {jlabel:18s} option {opt}:", r[0][1], r[0][3], "lambda free:", [x[5] for x in r])

print()
print("=== 3. Generator with the transversality of Martin1 2.1.3 item 3: J(n,e_i)=0 ===")
y1, y2 = sp.symbols('y1 y2')
# Tangents e1,e2 in CP2 and M4 such that J(CP2)(n_C,e)=0 and h(n,e)=0.
nC = n_warp[4:, 0]
InC = I4*nC
print("n_C =", list(nC), " I n_C =", list(InC), " n_C.I n_C =", (nC.T*InC)[0])
# e1 and e2 are orthogonal to n_C and to I n_C inside CP2, so they span the complex line orthogonal to n_C.
e1 = sp.Matrix([0, 0, 1, 0, 0, 0, 1, 0])
e2 = sp.Matrix([0, 0, 0, 1, 0, 0, 0, 1])
T = sp.Matrix.hstack(n_warp, e1, e2)
print("h(n,e1), h(n,e2) =", (n_warp.T*h*e1)[0], (n_warp.T*h*e2)[0])
V, P, na = Vof(JC, T)
print("pull J^C =", P.tolist(), " n^alpha =", list(na), " V =", list(V))
EC = 2*JC*V
print("E^C_k =", list(EC), "  = 4 J12 I n_C with J12 =", P[1, 2])
print("|E^C| != 0 although E^C is orthogonal to all tangents:", list(EC.T*T))

print()
print("=== 4. Branch free K-C-S with warped n, J^C != 0, V_C = 0 (non-transversal) ===")
# X3 tangent: n, e1 in the CP2 plane of n_C, e2 pure spacelike along the J(M4) kernel z
e1 = sp.Matrix([3, 5, 0, 0, 0, 1, 0, 0])      # J^C(n,e1) != 0, CP2 image stays in the plane (0,1)
e2 = sp.Matrix([0, 0, 0, 1, 0, 0, 0, 0])
print("h(n,e1), h(n,e2) =", (n_warp.T*h*e1)[0], (n_warp.T*h*e2)[0])
T = sp.Matrix.hstack(n_warp, e1, e2)
V, P, na = Vof(JC, T)
print("pull J^C:", P.tolist(), "n^alpha", list(na), "V", list(V), "E^C", list(2*JC*V))
print("kernel of J^C on X3 is e2, the null generator n carries J(n,e1) =", P[0, 1])

print()
print("=== 5. Interior Kahler flux has the K-C-S direction, block with d=2 ===")
v, a, b, c, j = sp.symbols('v a b c j', positive=True)
# (s,v) block A=a v^2, B=b v, C=-c, J_vs=j v
A, B, C = a*v**2, b*v, -c
D = sp.simplify(A*C - B**2)
Jvs = j*v
# J^{vs} = (g^vv g^ss - g^vs g^vs) J_vs = J_vs/D
sq = sp.sqrt(sp.Abs(D))
print("d=2 sqrt|D| J^vs limit v->0+ :", sp.simplify(sp.limit(sq*Jvs/D, v, 0)))
A1, B1 = a*v, b*v
D1 = sp.simplify(A1*C - B1**2)
sq1 = sp.sqrt(sp.Abs(D1))
print("d=1 sqrt|D| J^vs limit v->0+ :", sp.simplify(sp.limit(sq1*Jvs/D1, v, 0)))

print()
print("=== 6. Warped n, option a, J(M4) full: frame built to absorb lambda n_k ===")
J = Jblock(Jm_fu, I4)
Vd = J.inv()*(h*n_warp)
print("V = J^-1 h n =", list(Vd), " h(V,n) =", (Vd.T*h*n_warp)[0])
e = tangent_orth(n_warp)
T = sp.Matrix.hstack(n_warp, Vd, e)
print("pull J:", pull(J, T).tolist())
Ef = E(J, T)
ratio = [Ef[i]/(h*n_warp)[i] for i in range(8) if (h*n_warp)[i] != 0]
print("E_k / n_k on the nonzero components:", ratio)
print("Transversal? J(n,e) =", (n_warp.T*J*e)[0], " nonzero, so ker J on X3 is V and not n")
print("Eigenvector test: J n = mu h n would need I n_C = mu n_C, impossible for real mu when n_C != 0")
