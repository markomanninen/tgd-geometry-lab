# Twistor space of the conformally flat, non-Einstein base R x S^3.
# G = R x SU(2) x SU(2), H = U(1) in the diagonal. S^3 is the symmetric space
# (SU(2)xSU(2))/diag, so its Levi-Civita connection is the canonical one and
# Lambda^+(R x S^3) = T S^3 as an SO(3) bundle with that connection.
import sympy as sp, itertools
from a_homogeeninen import Homog, ip, I

pauli = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])]


def blk(a, b, c):
    M = sp.zeros(5)
    M[0:2, 0:2] = a
    M[2:4, 2:4] = b
    M[4, 4] = c
    return M


Z2 = sp.zeros(2)
T = [I * s / 2 for s in pauli]  # [T1,T2] = -T3 type, unit-speed rotation at twice angle


def L(i):
    return blk(T[i], Z2, 0)


def Rr(i):
    return blk(Z2, T[i], 0)


minus = [L(i) - Rr(i) for i in range(3)]
plus = [L(i) + Rr(i) for i in range(3)]
t = blk(Z2, Z2, I)
print("norms", ip(minus[0], minus[0]), ip(plus[0], plus[0]), ip(t, t))
# orthonormalise for ip
nm = sp.sqrt(ip(minus[0], minus[0]))
np_ = sp.sqrt(ip(plus[0], plus[0]))
nt = sp.sqrt(ip(t, t))
e = [t / nt] + [m / nm for m in minus] + [plus[0] / np_, plus[1] / np_]
hb = [(plus[2], ip(plus[2], plus[2]))]
y, c = sp.symbols("y c", positive=True)
S = Homog(e, [1, c, c, c, y, y], hb)
Rc = S.ric()
print("Ric diag (coordinate frame)", [sp.factor(Rc[i, i]) for i in range(6)])
print("Ric offdiag", {(i, j): sp.factor(Rc[i, j]) for i in range(6) for j in range(i + 1, 6) if Rc[i, j] != 0})
print("scalar", sp.factor(S.scal(Rc)))


def Jmat(pairs_signs):
    J = sp.zeros(6)
    for (p, q), s, in pairs_signs:
        # unit-length frames: J maps e_p/|e_p| to s e_q/|e_q|
        ratio = sp.sqrt(S.s[q]) / sp.sqrt(S.s[p])
        J[q, p] = s * ratio
        J[p, q] = -s / ratio
    return J


# Fibre point u fixed by H: plus[2] direction, so S^2 tangent is (4,5) and the
# tangent structure on the base pairs t with e3 and e1 with e2.
for s1, s2, s3 in itertools.product((1, -1), (1, -1), (1,)):
    J = Jmat([((0, 3), s1), ((1, 2), s2), ((4, 5), s3)])
    # H-invariance of J is required for a well defined structure
    inv = all((S.hpart[0][0] * J - J * S.hpart[0][0]).applyfunc(sp.simplify)[i, j] == 0 for i in range(6) for j in range(6))
    gm = sp.diag(*S.s)
    Jric = (J.T * Rc * J - Rc).applyfunc(sp.simplify)
    w = gm * J
    dw = {}
    for i, j, k in itertools.combinations(range(6), 3):
        v = 0
        for a, b, d in ((i, j, k), (j, k, i), (k, i, j)):
            v -= sum(S.c[a][b][l] * w[l, d] for l in range(6))
        v = sp.simplify(v)
        if v != 0:
            dw[(i, j, k)] = v

    def br(a, b):
        r = sp.zeros(6, 1)
        for p in range(6):
            for q in range(6):
                if a[p] != 0 and b[q] != 0:
                    for l in range(6):
                        r[l] += a[p] * b[q] * S.c[p][q][l]
        return r

    Nn = 0
    for i in range(6):
        for j in range(6):
            Xv, Yv = sp.eye(6)[:, i], sp.eye(6)[:, j]
            JX, JY = J * Xv, J * Yv
            N = br(JX, JY) - br(Xv, Yv) - J * br(JX, Yv) - J * br(Xv, JY)
            Nn += sum(v**2 for v in N)
    # note: the Nijenhuis test above drops the h-part, which vanishes on an H-invariant J
    print("signs", (s1, s2, s3), "Nijenhuis^2", sp.simplify(Nn),
          "| Ric(J,J)-Ric nonzero entries", {(i, i): sp.factor(Jric[i, i]) for i in range(6) if Jric[i, i] != 0},
          "| dw", set(sp.factor(v) for v in dw.values()))
