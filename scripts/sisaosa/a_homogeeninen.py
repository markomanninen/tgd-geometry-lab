# Exact curvature of reductive homogeneous spaces G/H with a block-diagonal
# invariant metric, independent of any Kaluza-Klein formula.
# Besse 7.28-7.30: Lambda(X)Y = 1/2 [X,Y]_m + U(X,Y),
# 2<U(X,Y),Z> = <[Z,X]_m,Y> + <X,[Z,Y]_m>,
# R(X,Y)Z = L(X)L(Y)Z - L(Y)L(X)Z - L([X,Y]_m)Z - [[X,Y]_h,Z].
import sympy as sp
import itertools, sys

I = sp.I


def E(n, i, j):
    M = sp.zeros(n)
    M[i, j] = 1
    return M


def ip(A, B):
    # -1/2 tr(AB) on anti-Hermitian matrices, real
    return sp.nsimplify(sp.expand(-(A * B).trace() / 2))


class Homog:
    def __init__(self, m_basis, scales, h_basis):
        # m_basis orthonormal for ip, scales = squared lengths in the metric
        self.m, self.h, self.s = m_basis, h_basis, scales
        self.n = len(m_basis)
        n = self.n
        # bracket coefficients in the ip-orthonormal basis
        self.c = [[[0] * n for _ in range(n)] for _ in range(n)]  # [e_i,e_j]_m = c[i][j][k] e_k
        self.hpart = [[None] * n for _ in range(n)]  # [[e_i,e_j]_h, e_k] coefficients
        for i in range(n):
            for j in range(n):
                br = m_basis[i] * m_basis[j] - m_basis[j] * m_basis[i]
                for k in range(n):
                    self.c[i][j][k] = ip(br, m_basis[k])
                hcomp = sp.zeros(*br.shape)
                for hb, hn in h_basis:
                    hcomp += ip(br, hb) / hn * hb
                mat = sp.zeros(n)
                for k in range(n):
                    b2 = hcomp * m_basis[k] - m_basis[k] * hcomp
                    for l in range(n):
                        mat[l, k] = ip(b2, m_basis[l])
                self.hpart[i][j] = mat
        self.build()

    def build(self):
        n, c, s = self.n, self.c, self.s
        # connection matrices L[i][k, j] = component k of Lambda(e_i) e_j
        self.L = []
        for i in range(n):
            M = sp.zeros(n)
            for j in range(n):
                for k in range(n):
                    # <Lambda(e_i)e_j, e_k> in the metric
                    # 2<U(X,Y),Z> = <[Z,X]_m,Y>+<X,[Z,Y]_m>
                    U = sp.Rational(1, 2) * (c[k][i][j] * s[j] + c[k][j][i] * s[i])
                    val = sp.Rational(1, 2) * c[i][j][k] * s[k] + U
                    M[k, j] = sp.cancel(val / s[k])
            self.L.append(M)
        # curvature R[i][j] matrix acting on m
        self.R = [[None] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                M = self.L[i] * self.L[j] - self.L[j] * self.L[i]
                for k in range(n):
                    if c[i][j][k] != 0:
                        M -= c[i][j][k] * self.L[k]
                M -= self.hpart[i][j]
                self.R[i][j] = M.applyfunc(sp.cancel)

    def ric(self):
        n = self.n
        Rc = sp.zeros(n)
        for j in range(n):
            for k in range(n):
                # Ric(e_j,e_k) = sum_i <R(e_i,e_j)e_k,e_i>/g_ii
                Rc[j, k] = sp.cancel(sum(self.R[i][j][i, k] for i in range(n)))
        return Rc

    def scal(self, Rc=None):
        Rc = self.ric() if Rc is None else Rc
        return sp.cancel(sum(Rc[i, i] / self.s[i] for i in range(self.n)))


def su3():
    n = 3
    def pair(a, b):
        return [E(n, a, b) - E(n, b, a), I * (E(n, a, b) + E(n, b, a))]
    # roots: base (0,1), (0,2); fibre (1,2) of F -> CP2 with point L_0
    m = pair(0, 1) + pair(0, 2) + pair(1, 2)
    h = [I * (E(n, 0, 0) - E(n, 1, 1)), I * (E(n, 1, 1) - E(n, 2, 2))]
    # orthogonalise h
    h0 = h[0]
    h1 = h[1] - ip(h[1], h0) / ip(h0, h0) * h0
    return m, [(h0, ip(h0, h0)), (h1, ip(h1, h1))]


def sp2_blocks():
    # sp(2) in 4x4 complex: quaternion (a,b) as [[a,b],[-conj b, conj a]]
    def Q(q):
        a, b, c, d = q
        return sp.Matrix([[a + I * b, c + I * d], [-c + I * d, a - I * b]])

    def blk(A, B, C, D):
        return sp.Matrix(sp.BlockMatrix([[A, B], [C, D]]))

    Z = sp.zeros(2)
    im = [(0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]
    all4 = [(1, 0, 0, 0)] + im
    # p: [[0,q],[-qbar,0]] -> base S^4 tangent
    p = []
    for q in all4:
        A = Q(q)
        p.append(blk(Z, A, -A.H, Z))
    # sp(1) x sp(1): diagonal blocks
    upper = [blk(Q(q), Z, Z, Z) for q in im]
    lower = [blk(Z, Z, Z, Q(q)) for q in im]
    return p, upper, lower


def normalise(M):
    return M / sp.sqrt(ip(M, M))


if __name__ == "__main__":
    y = sp.symbols("y", positive=True)
    print("== F = SU(3)/T^2, metric 1 on two base root planes, y on the fibre root plane ==")
    m, h = su3()
    m = [normalise(a) for a in m]
    print("norms", [ip(a, a) for a in m])
    F = Homog(m, [1, 1, 1, 1, y, y], h)
    Rc = F.ric()
    print("Ric diag", [sp.factor(Rc[i, i]) for i in range(6)])
    print("Ric off-diagonal all zero:", all(Rc[i, j] == 0 for i in range(6) for j in range(6) if i != j))
    s = F.scal(Rc)
    print("scalar", sp.factor(s), " prediction 24+8/y-2y diff:", sp.simplify(s - (24 + 8 / y - 2 * y)))
    print("y=1", s.subs(y, 1), " y=2", s.subs(y, 2))
    print("Einstein values of y:", sp.solve(sp.Eq(sp.cancel(Rc[0, 0]), sp.cancel(Rc[4, 4] / y)), y))

    # Almost complex structures: signs (e1,e2,e3) on the three root planes
    def Jmat(e):
        J = sp.zeros(6)
        for b, sgn in zip((0, 2, 4), e):
            J[b + 1, b] = sgn
            J[b, b + 1] = -sgn
        return J

    gm = sp.diag(1, 1, 1, 1, y, y)

    def dform(w):
        # invariant 2-form w (antisym matrix in m basis), dw(X,Y,Z) = -w([X,Y]_m,Z)-cyc
        out = {}
        for i, j, k in itertools.combinations(range(6), 3):
            v = 0
            for a, b, c in ((i, j, k), (j, k, i), (k, i, j)):
                v -= sum(F.c[a][b][l] * w[l, c] for l in range(6))
            v = sp.cancel(v)
            if v != 0:
                out[(i, j, k)] = v
        return out

    def nijenhuis(J):
        n = 0
        for i in range(6):
            for j in range(6):
                # N(X,Y) = [JX,JY]_m+... evaluated with Lambda: use torsion free covariant form
                X = sp.eye(6)[:, i]
                Y = sp.eye(6)[:, j]
                JX, JY = J * X, J * Y
                def br(a, b):
                    r = sp.zeros(6, 1)
                    for p in range(6):
                        for q in range(6):
                            if a[p] != 0 and b[q] != 0:
                                for l in range(6):
                                    r[l] += a[p] * b[q] * F.c[p][q][l]
                    return r
                N = br(JX, JY) - br(X, Y) - J * br(JX, Y) - J * br(X, JY)
                n += sum(v**2 for v in N)
        return sp.simplify(n)

    sols = {}
    for e in itertools.product((1, -1), repeat=3):
        if e[2] == -1:
            continue  # overall sign
        J = Jmat(e)
        w = (gm * J)  # g(J X, Y) up to sign
        dw = dform(w)
        Nn = nijenhuis(J)
        # (1,1) defects
        Jt = J
        ric_def = (Jt.T * Rc * Jt - Rc).applyfunc(sp.cancel)
        riem_def = 0
        for a in range(6):
            for b in range(6):
                C = (F.R[a][b] * J - J * F.R[a][b]).applyfunc(sp.cancel)
                riem_def += sum(v**2 / 1 for v in C)
        riem_def = sp.factor(sp.cancel(riem_def))
        print("J signs", e, "Nijenhuis^2 =", Nn, "| Ric(J,J)-Ric all zero:", all(v == 0 for v in ric_def),
              "| dw comps", set(sp.factor(v) for v in dw.values()), "| sum |[R,J]|^2 =", riem_def)

    print("== closed invariant 2-forms on F ==")
    a1, a2, a3 = sp.symbols("a1 a2 a3")
    w = sp.zeros(6)
    for b, c in zip((0, 2, 4), (a1, a2, a3)):
        w[b + 1, b] = c
        w[b, b + 1] = -c
    dw = dform(w)
    print("dw components", set(sp.factor(v) for v in dw.values()))

    print("== CP^3 = Sp(2)/Sp(1)U(1), S^4 base ==")
    p, up, lo = sp2_blocks()
    p = [normalise(a) for a in p]
    up = [normalise(a) for a in up]
    lo = [normalise(a) for a in lo]
    print("p norms", [ip(a, a) for a in p], "fibre norms", [ip(a, a) for a in up])
    # fibre direction: two generators of upper sp(1); H = u(1) x lower sp(1)
    hb = [(up[0], ip(up[0], up[0]))] + [(a, ip(a, a)) for a in lo]
    C = Homog(p + up[1:], [1, 1, 1, 1, y, y], hb)
    RcC = C.ric()
    sc = C.scal(RcC)
    print("Ric diag", [sp.factor(RcC[i, i]) for i in range(6)])
    print("scalar", sp.factor(sc))

    print("== S^7 = Sp(2)/Sp(1), fibre S^3 ==")
    hb = [(a, ip(a, a)) for a in lo]
    S = Homog(p + up, [1, 1, 1, 1, y, y, y], hb)
    RcS = S.ric()
    ss = S.scal(RcS)
    print("Ric diag", [sp.factor(RcS[i, i]) for i in range(7)])
    print("scalar", sp.factor(ss))
