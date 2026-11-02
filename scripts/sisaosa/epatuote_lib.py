# Shared numerics for the non-product string ansatz.
# Units: a = R^2/4 = 1, so K(CP1) = 1, R^2 = 4, area(CP1) = 4 pi.
# Embedding: t, z, rho(s) e^{i m phi} ; Theta(s), Phi = n phi + omega t + k z.
# Reduced Lagrangian in units 1/(16 pi G), per unit phi:
#   L = 2 Lam N P + M + 2 (P'/N)'   with
#   M = mu p' W' / (2 N P), P^2 = p (1 - mu W) + n^2 W, p = m^2 rho^2, W = sin^2 Theta.
# After integrating phi: 8 G T = int ds L.
import numpy as np
from scipy.integrate import solve_ivp


class Par:
    def __init__(self, Lam, mu, m=1, n=1):
        self.Lam, self.mu, self.m, self.n = Lam, mu, m, n


def PP(x, y, q):
    return np.sqrt(q.m**2 * x**2 * (1 - q.mu * np.sin(y)**2) + q.n**2 * np.sin(y)**2)


def f_all(x, y, b, q):
    """Density f(x,y,beta) and the partial derivatives needed in the curve equation."""
    Lam, mu, m, n = q.Lam, q.mu, q.m, q.n
    W = np.sin(y)**2
    Wy = np.sin(2*y)
    Wyy = 2*np.cos(2*y)
    p = m**2 * x**2
    px = 2*m**2*x
    P2 = np.maximum(p*(1 - mu*W) + n**2*W, 1e-14)
    P = np.sqrt(P2)
    Px = px*(1 - mu*W)/(2*P)
    Py = (-p*mu*Wy + n**2*Wy)/(2*P)
    # M0 = mu px Wy / (2 P); M = M0 cos(b) sin(b)
    M0 = mu*px*Wy/(2*P)
    M0x = mu*2*m**2*Wy/(2*P) - M0*Px/P
    M0y = mu*px*Wyy/(2*P) - M0*Py/P
    c, s = np.cos(b), np.sin(b)
    cs = c*s
    f = 2*Lam*P + M0*cs
    fx = 2*Lam*Px + M0x*cs
    fy = 2*Lam*Py + M0y*cs
    fb = M0*(c*c - s*s)
    fbx = M0x*(c*c - s*s)
    fby = M0y*(c*c - s*s)
    fbb = -4*M0*cs
    return f, fx, fy, fb, fbx, fby, fbb, P


def rhs(s, u, q):
    x, y, b, *_ = u
    f, fx, fy, fb, fbx, fby, fbb, P = f_all(x, y, b, q)
    c, sn = np.cos(b), np.sin(b)
    num = fy*c - fx*sn - fby*sn - fbx*c
    den = f + fbb
    db = num/den
    # accumulators: I_area = int 2 Lam P, I_M = int M, I_dmu = int d_mu (2 Lam P + M)
    W = np.sin(y)**2
    Wy = np.sin(2*y)
    p = q.m**2*x**2
    px = 2*q.m**2*x
    area = P
    M = q.mu*px*c*Wy*sn/(2*P)
    dmu = -q.Lam*p*W/P + px*c*Wy*sn/(2*P) + q.mu*px*c*Wy*sn*p*W/(4*P**3)
    return [c, sn, db, area, M, dmu]


def start(b0, s0, y0=0.0, q=None):
    """Regular start at the axis point (rho=0, Theta=y0) with direction b0."""
    return [s0*np.cos(b0), y0 + s0*np.sin(b0), b0, 0.0, 0.0, 0.0]


def integrate(b0, q, smax, s0=1e-3, y0=0.0, events=None, rtol=1e-10, atol=1e-11, dense=False):
    u0 = start(b0, s0, y0, q)
    sol = solve_ivp(rhs, [s0, smax], u0, args=(q,), method='DOP853', rtol=rtol, atol=atol,
                    events=events, dense_output=dense)
    return sol


def geom(x, y, b, q):
    """Return metric block data along the curve in arc length gauge N=1."""
    return dict(P=PP(x, y, q))


def metric_at(xf, yf, sv, om, k, q):
    """Full 4x4 metric at s from callables xf, yf (coordinates t,z,s,phi; N=1 gauge not assumed)."""
    x, y = xf(sv), yf(sv)
    W = np.sin(y)**2
    p = q.m**2*x**2
    v = np.array([om, k, 0.0, q.n])
    return x, y, p, W, v


def einstein_direct(gfun, sv, h=2e-3):
    """Direct G^{ab}, R, Gamma at s=sv from a metric function gfun(s) (4x4, depends on s only).
    Derivatives by 8th order central differences. Nothing from the reduced action is used."""
    st = np.array([-4, -3, -2, -1, 1, 2, 3, 4], float)
    c1 = np.array([1/280, -4/105, 1/5, -4/5, 4/5, -1/5, 4/105, -1/280])
    gs = {j: gfun(sv + j*h) for j in st}
    g = gfun(sv)
    dg = sum(c*gs[j] for c, j in zip(c1, st))/h
    c2 = np.array([-1/560, 8/315, -1/5, 8/5, 8/5, -1/5, 8/315, -1/560])
    ddg = (sum(c*gs[j] for c, j in zip(c2, st)) - (205/72)*g)/h**2
    S = 2
    ginv = np.linalg.inv(g)
    dginv = -ginv @ dg @ ginv
    # partial derivative array dG[c][a,b] = d_c g_ab, nonzero only for c = S
    D = np.zeros((4, 4, 4))
    D[S] = dg
    DD = np.zeros((4, 4, 4))
    DD[S] = ddg
    # low[d,b,c] = 0.5( d_c g_db + d_b g_dc - d_d g_bc)
    low = np.zeros((4, 4, 4))
    dlow = np.zeros((4, 4, 4))
    for d in range(4):
        for b in range(4):
            for c in range(4):
                low[d, b, c] = 0.5*(D[c, d, b] + D[b, d, c] - D[d, b, c])
                dlow[d, b, c] = 0.5*(DD[c, d, b] + DD[b, d, c] - DD[d, b, c])
    Gam = np.einsum('ad,dbc->abc', ginv, low)
    dGam = np.einsum('ad,dbc->abc', dginv, low) + np.einsum('ad,dbc->abc', ginv, dlow)
    # Ricci R_bd = d_a Gam^a_bd - d_d Gam^a_ba + Gam^a_ae Gam^e_bd - Gam^a_de Gam^e_ba
    Ric = np.zeros((4, 4))
    for b in range(4):
        for d in range(4):
            t1 = dGam[S, b, d]
            t2 = dGam[:, b, :].trace() if d == S else 0.0
            t3 = np.einsum('aae,e->', Gam, Gam[:, b, d])
            t4 = sum(Gam[a, d, e]*Gam[e, b, a] for a in range(4) for e in range(4))
            Ric[b, d] = t1 - t2 + t3 - t4
    Rs = np.sum(ginv*Ric)
    Eup = ginv @ (Ric - 0.5*Rs*g) @ ginv
    return dict(g=g, ginv=ginv, Gam=Gam, Ric=Ric, R=Rs, Gup=Eup)


def direct_check(sol, s_pts, om, k, q, h=2e-3):
    """At each s in s_pts return G^{ab}, direct field equation residual, tangency of B, and sqrt|g|P^tt data.
    sol.sol is the dense output in arc length gauge. Only the embedding functions are used."""
    n, m = q.n, q.m
    v = np.array([om, k, 0.0, n])

    def gfun(sv):
        x, y = sol.sol(sv)[:2]
        W = np.sin(y)**2
        p = m**2*x**2
        return np.diag([1.0, -1.0, -1.0, -p]) - W*np.outer(v, v)

    out = []
    for sv in s_pts:
        E = einstein_direct(gfun, sv, h)
        x, y, b = sol.sol(sv)[:3]
        st = np.array([-2, -1, 1, 2], float)
        c1 = np.array([1/12, -2/3, 2/3, -1/12])
        c2 = np.array([-1/12, 4/3, 4/3, -1/12])
        xs = np.array([sol.sol(sv+j*h)[:2] for j in st])
        d1 = (c1 @ xs)/h
        d2 = ((c2 @ xs) - 2.5*np.array([x, y]))/h**2
        # target coordinates (T, Z, X, Y, Th, Ph) at t=z=phi=0
        cf, sf = 1.0, 0.0
        dh = np.zeros((4, 6))
        dh[0] = [1, 0, 0, 0, 0, om]
        dh[1] = [0, 1, 0, 0, 0, k]
        dh[2] = [0, 0, d1[0], 0, d1[1], 0]
        dh[3] = [0, 0, 0, m*x, 0, n]
        ddh = np.zeros((4, 4, 6))
        ddh[2, 2] = [0, 0, d2[0], 0, d2[1], 0]
        ddh[2, 3] = ddh[3, 2] = [0, 0, 0, m*d1[0], 0, 0]
        ddh[3, 3] = [0, 0, -m**2*x, 0, 0, 0]
        Gam = E['Gam']
        B = np.zeros((4, 4, 6))
        for a in range(4):
            for c in range(4):
                B[a, c] = ddh[a, c] - sum(Gam[e, a, c]*dh[e] for e in range(4))
                # target connection of the unit sphere
                u, w = dh[a], dh[c]
                B[a, c, 4] += -np.sin(y)*np.cos(y)*u[5]*w[5]
                B[a, c, 5] += (np.cos(y)/np.sin(y))*(u[4]*w[5] + u[5]*w[4])
        Tg = E['Gup'] - q.Lam*E['ginv']
        Res = np.einsum('ab,abk->k', Tg, B)
        Gpart = np.einsum('ab,abk->k', E['Gup'], B)
        # tangency: B must be orthogonal to the tangent space in the target metric
        tm = np.diag([1, -1, -1, -1, -1, -np.sin(y)**2])
        tang = np.einsum('abk,kl,cl->abc', B, tm, dh)
        P = np.sqrt(abs(np.linalg.det(E['g'])))
        out.append(dict(s=sv, x=x, y=y, R=E['R'], Gtt=E['Gup'][0, 0], gtt=E['ginv'][0, 0],
                        Gzz=E['Gup'][1, 1], gzz=E['ginv'][1, 1], Gtz=E['Gup'][0, 1], gtz=E['ginv'][0, 1],
                        res=np.max(np.abs(Res)), gp=np.max(np.abs(Gpart)), tang=np.max(np.abs(tang)), P=P))
    return out
