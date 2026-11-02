# Edges for pure volume: conormal balance, null kinks, determinism count, Euclidean energy.
import numpy as np, sympy as sp
rng = np.random.default_rng(3)

print("=== 1. Killing fields of SU(3) span T CP2 at a random point ===")
gm = np.zeros((8, 3, 3), complex)
gm[0][0, 1] = gm[0][1, 0] = 1
gm[1][0, 1] = -1j; gm[1][1, 0] = 1j
gm[2][0, 0] = 1; gm[2][1, 1] = -1
gm[3][0, 2] = gm[3][2, 0] = 1
gm[4][0, 2] = -1j; gm[4][2, 0] = 1j
gm[5][1, 2] = gm[5][2, 1] = 1
gm[6][1, 2] = -1j; gm[6][2, 1] = 1j
gm[7] = np.diag([1, 1, -2])/np.sqrt(3)
z = rng.normal(size=3)+1j*rng.normal(size=3)
z /= np.linalg.norm(z)
rows = []
for l in gm:
    dz = 1j*l@z
    # affine coordinates xi = z1/z0, z2/z0
    xi = np.array([z[1]/z[0], z[2]/z[0]])
    dxi = np.array([(dz[1]-xi[0]*dz[0])/z[0], (dz[2]-xi[1]*dz[0])/z[0]])
    rows.append([dxi[0].real, dxi[0].imag, dxi[1].real, dxi[1].imag])
print("rank of 8 Killing vectors in T CP2:", np.linalg.matrix_rank(np.array(rows)))
print("Together with M4 translations every H component of the conormal is seen.")

print()
print("=== 2. Two-sheet edge in M4 x S1: xi = w_pm t + q_pm x ===")
w1, w2, q1, q2 = sp.symbols('w1 w2 q1 q2', real=True)
def cur(w, q, normal):
    # graph xi=w t+q x in (t,x); metric m - df df on (t,x)
    g = sp.Matrix([[1-w**2, -w*q], [-w*q, -1-q**2]])
    D = -g.det()
    gi = g.inv()
    sq = sp.sqrt(D)
    a = 0 if normal == 't' else 1
    jt = sq*gi[a, 0]                              # d_b t = delta_b^t, current of translation t
    jx = sq*gi[a, 1]
    jxi = sq*(gi[a, 0]*w+gi[a, 1]*q)
    return [sp.simplify(c) for c in (jt, jx, jxi)]
for n, surf in (('t', 'edge t=0 (timelike normal): continuity of xi forces q1=q2=q'), ('x', 'edge x=0 (spacelike normal): continuity of xi forces w1=w2=w')):
    print(surf)
    if n == 't':
        a = cur(w1, q2, 't'); b = cur(w2, q2, 't')
        print("  j^t_t, j^t_x, j^t_xi =", a)
        vals = {w1: sp.Rational(1, 2), q2: sp.Rational(1, 3)}
        tv = sp.Rational(1, 5)
        print("  numeric differences at w1=1/2, w2=1/5, q=1/3:",
              [float((x-y).subs({w1: sp.Rational(1, 2), w2: tv, q2: sp.Rational(1, 3)})) for x, y in zip(a, b)])
    else:
        a = cur(w2, q1, 'x'); b = cur(w2, q2, 'x')
        print("  numeric differences at q1=1/2, q2=1/5, w=1/3:",
              [float((x-y).subs({q1: sp.Rational(1, 2), q2: sp.Rational(1, 5), w2: sp.Rational(1, 3)})) for x, y in zip(a, b)])

print()
print("=== 3. Junctions of k sheets, unit conormals in the normal space of X3 ===")
def unit_time(p):
    return np.array([np.sqrt(1+p@p), *p])
def mink(a, b):
    return a[0]*b[0]-a[1:]@b[1:]
# 1 -> 2: norm of nu1+nu2 for future unit vectors
vals = []
for _ in range(20000):
    a, b = unit_time(rng.normal(size=4)), unit_time(rng.normal(size=4))
    s = a+b
    vals.append(np.sqrt(mink(s, s)))
print("1->2 timelike normal: min |nu1+nu2| over samples =", min(vals), "(needs 1)")
# 2 -> 2 example with M4 x CP2 normal space (1,4)
p = np.array([0.7, 0.2, 0, 0]); q = np.array([-0.7, -0.2, 0, 0])
a, b = unit_time(p), unit_time(q)
rot = np.array([[0, 1], [-1, 0]])
p2 = p.copy(); p2[:2] = rot@p[:2]; q2_ = -p2
c, d = unit_time(p2), unit_time(q2_)
print("2->2 example residual nu1+nu2-nu3-nu4 =", np.round(a+b-c-d, 12))
th = 2*np.pi/3
ys = [np.array([np.cos(i*th), np.sin(i*th)]) for i in range(3)]
print("3 sheets spacelike normal, residual of 120 degree junction =", np.round(sum(ys), 12))

print()
print("=== 4. Null kink, xi = f(u), u=t-z, v=t+z, in M4 x S1 ===")
U, V, X, Y = sp.symbols('u v x y', real=True)
fp = sp.Symbol('fp', real=True)
# coordinates (u,v,x,y): m = du dv - dx^2 - dy^2, xi = f(u): g_uu = -fp^2, g_uv=1/2
g = sp.Matrix([[-fp**2, sp.Rational(1, 2), 0, 0], [sp.Rational(1, 2), 0, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]])
gi = g.inv()
print("g^uu, g^uv, g^vv =", gi[0, 0], gi[0, 1], gi[1, 1], " det g =", g.det())
print("normal current through u=const: sqrt|g| g^{ub} d_b h = (1/2)*2*d_v h, no dependence on f', so it is continuous over a kink of f")
print("xi component of j^u: sqrt|g| (g^uu fp + g^uv*0) =", gi[0, 0]*fp, "= 0")
print("j^v_xi = (1/2) g^vu fp =", sp.Rational(1, 2)*gi[1, 0]*fp, " jumps but it is tangential to u=const")
print("c_#^2 = g_tt = 1 - fp^2, so the kink changes c_#:", 1-sp.Rational(1, 4), "->", 1-sp.Rational(9, 16))

print()
print("=== 5. CP2 type piece for pure volume: m^k=f^k(u(s)), g=-s ===")
print("Eq.: Delta u f' + |grad u|^2 f'' = 0, so f'' || f' (straight null line, same as massa.md for Lambda != k).")
print("Energy rule of massa.md with k=0: E dt = -c_V int |grad t|^2 dV < 0 in the Euclidean region.")

