# Shared library for the X^6 calculation: F = T(CP2) as incidence variety, target spaces, curvature by autodiff.
# F = {(z,xi) in CP2 x CP2* : z.xi = 0}.  Twistor projection p = conj(z) x xi (non-holomorphic).
# Chart (zeta,s,tau): z=(-tau, zeta+s tau, 1), xi=(s,1,-zeta).  zeta=-xi2/xi1 is the fibre coordinate.
# Metric g_F = |th13|^2 + |th23|^2 + y |th12|^2, y=2 is the Kaehler-Einstein point, R(CP2 units): Ric=6g.
import jax, jax.numpy as jnp, numpy as np
jax.config.update("jax_enable_x64", True)
c = lambda a, b: a + 1j * b
nrm = lambda v: jnp.sqrt(jnp.sum(jnp.real(v * jnp.conj(v))))
herm = lambda u, v: jnp.sum(u * jnp.conj(v), axis=-1)

def zxi_chart(zeta, s, tau):
    z = jnp.stack([-tau, zeta + s * tau, jnp.ones_like(zeta)])
    xi = jnp.stack([s, jnp.ones_like(zeta), -zeta])
    return z, xi

def frames(z, xi):
    p = jnp.cross(jnp.conj(z), xi)
    return z / nrm(z), jnp.conj(xi) / nrm(xi), p / nrm(p)

def pull_F(zxi_fun, x, y):
    """pull back g_F(y) under x -> (z,xi); returns real symmetric matrix in x-coordinates"""
    f = lambda x_: jnp.concatenate(frames(*zxi_fun(x_)))
    E = f(x)
    dE = jax.jacfwd(f)(x)  # 9 x n, complex
    e1, e2, e3 = E[:3], E[3:6], E[6:]
    d1, d2, d3 = dE[:3], dE[3:6], dE[6:]
    t12 = jnp.conj(e2) @ d1
    t13 = jnp.conj(e3) @ d1
    t23 = jnp.conj(e3) @ d2
    o = lambda t: jnp.real(jnp.outer(t, jnp.conj(t)))
    return o(t13) + o(t23) + y * o(t12)

def fs(W_fun, x):
    """Fubini-Study pullback of W_fun: x -> C^n, holomorphic curvature 4"""
    W = W_fun(x)
    dW = jax.jacfwd(W_fun)(x)
    n2 = jnp.sum(jnp.real(W * jnp.conj(W)))
    t = dW / jnp.sqrt(n2)
    a = jnp.real(jnp.conj(t).T @ t)
    v = jnp.conj(W) @ dW / n2
    return a - jnp.real(jnp.outer(jnp.conj(v), v))

def sphere(zeta):  # dOmega^2 in real coordinates of zeta
    return 4.0 / (1 + jnp.real(zeta * jnp.conj(zeta))) ** 2 * jnp.eye(2)

# ---- target T: coordinates x = (m1,m2,m3,m4,zr,zi)
def eta(lorentz):
    if lorentz:  # (u,v,wr,wi), ds^2 = du dv - dwr^2 - dwi^2
        return jnp.array([[0, .5, 0, 0], [.5, 0, 0, 0], [0, 0, -1., 0], [0, 0, 0, -1.]])
    return jnp.eye(4)

def T_product(x, a, lorentz):
    G = jnp.zeros((6, 6))
    G = G.at[:4, :4].set(eta(lorentz))
    return G.at[4:, 4:].set(a * sphere(c(x[4], x[5])))

def Z12(x, lorentz):
    zeta = c(x[4], x[5])
    if lorentz:
        w = c(x[2], x[3]); u = x[0]; v = x[1]
        return w + zeta * u, v + zeta * jnp.conj(w)
    A = c(x[0], x[1]); B = c(x[2], x[3])
    return A + zeta * jnp.conj(B), B - zeta * jnp.conj(A)

def T_cp3(x, a):  # Euclidean: CP3 -> S^4 of radius l, a=l^2, fibre radius l.  Kaehler.
    l = jnp.sqrt(a)
    def W(x_):
        Z1, Z2 = Z12(x_, False)
        return jnp.stack([jnp.ones_like(Z1), c(x_[4], x_[5]), Z1 / (2 * l), Z2 / (2 * l)])
    return 4 * a * fs(W, x)

# ---- curvature of a metric function
def christoffel(g, x):
    G = g(x); Gi = jnp.linalg.inv(G); dG = jax.jacfwd(g)(x)  # dG[i,j,k] = d_k G_ij
    low = 0.5 * (jnp.einsum('kji->kij', dG) + jnp.einsum('kij->kij', dG) - jnp.einsum('ijk->kij', dG))
    return jnp.einsum('lk,kij->lij', Gi, low)

def ricci(g, x):
    Gam = lambda x_: christoffel(g, x_)
    Ga = Gam(x); dGa = jax.jacfwd(Gam)(x)  # dGa[l,i,j,k]=d_k Ga^l_ij
    return (jnp.einsum('lijl->ij', dGa) - jnp.einsum('lilj->ij', dGa)
            + jnp.einsum('llm,mij->ij', Ga, Ga) - jnp.einsum('ljm,mil->ij', Ga, Ga))

def scal(g, x):
    return jnp.einsum('ij,ij->', jnp.linalg.inv(g(x)), ricci(g, x))

def sqrtdet(g, x):
    return jnp.sqrt(jnp.abs(jnp.linalg.det(g(x))))

# ---- fibration by x4,x5 = const m: O'Neill A-tensor square and vertical/horizontal pieces
def split(g, x):
    G = g(x); h = G[4:, 4:]; hi = jnp.linalg.inv(h); C = G[:4, 4:]
    N = C @ hi  # N[mu,i]
    g4 = G[:4, :4] - N @ C.T
    return g4, h, N

def A2(g, x):
    """|A|^2 = 1/4 h_ij F^i_mn F^j^mn for the distribution orthogonal to the fibres m=const"""
    Nf = lambda x_: split(g, x_)[2]
    N = Nf(x); dN = jax.jacfwd(Nf)(x)  # dN[mu,i,k]
    dmu = dN[:, :, :4]; dv = dN[:, :, 4:]
    # F[mu,nu,i] = -d_mu N_nu^i + d_nu N_mu^i + N_mu^j d_j N_nu^i - N_nu^j d_j N_mu^i
    t = -jnp.einsum('nim->mni', dmu) + jnp.einsum('min->mni', dmu)
    u = jnp.einsum('mj,nij->mni', N, dv)
    F = t + u - jnp.einsum('mni->nmi', u)
    g4, h, _ = split(g, x)
    gi = jnp.linalg.inv(g4)
    return 0.25 * jnp.einsum('ij,mni,rsj,mr,ns->', h, F, F, gi, gi)

# ---- 12-D target and Euler-Lagrange expression (Ein^{ab}-Lam G^{ab}) H^A_ab
def ambient(Y, Tfun, b, y):
    """Y=(x0..x5, zeta'r,zeta'i,sr,si,taur,taui)"""
    G = jnp.zeros((12, 12)).at[:6, :6].set(Tfun(Y[:6]))
    f = lambda q: zxi_chart(c(q[0], q[1]), c(q[2], q[3]), c(q[4], q[5]))
    return G.at[6:, 6:].set(b * pull_F(f, Y[6:], y))

def el(embed, Tfun, b, y, x, lam=0.0):
    amb = lambda Y: ambient(Y, Tfun, b, y)
    def g(x_):
        J = jax.jacfwd(embed)(x_)
        return J.T @ amb(embed(x_)) @ J
    Y0 = embed(x); J = jax.jacfwd(embed)(x); ddY = jax.jacfwd(jax.jacfwd(embed))(x)
    GamA = christoffel(amb, Y0); Gam6 = christoffel(g, x)
    H = ddY + jnp.einsum('Abc,ba,cd->Aad', GamA, J, J) - jnp.einsum('gad,Ag->Aad', Gam6, J)
    Gi = jnp.linalg.inv(g(x)); Ric = ricci(g, x); R = jnp.einsum('ij,ij->', Gi, Ric)
    Ein = Gi @ Ric @ Gi - 0.5 * R * Gi
    Hv = jnp.einsum('ab,Aab->A', Gi, H)           # mean curvature vector
    Hb = H.reshape(12, 6, 6)
    E = jnp.einsum('ab,Aab->A', Ein, Hb) - lam * Hv
    Gamb = amb(Y0)
    tang = jnp.max(jnp.abs(J.T @ Gamb @ Hv))      # must vanish
    nr = lambda v: jnp.sqrt(jnp.abs(v @ Gamb @ v))
    return dict(H=Hv, E=E, H_size=jnp.max(jnp.abs(Hv)), E_size=jnp.max(jnp.abs(E)), tang=tang, R=R)

def sph_grid(nth=12, nph=24):
    """Gauss-Legendre in cos(theta), uniform in phi: zeta=tan(th/2) e^{i ph}; weights sum to 4 pi"""
    t, w = np.polynomial.legendre.leggauss(nth)
    ph = (np.arange(nph) + .5) * 2 * np.pi / nph
    zs, ws = [], []
    for ti, wi in zip(t, w):
        r = np.sqrt((1 - ti) / (1 + ti))
        for p in ph:
            zs.append((r * np.cos(p), r * np.sin(p))); ws.append(wi * 2 * np.pi / nph)
    return jnp.array(zs), jnp.array(ws)
