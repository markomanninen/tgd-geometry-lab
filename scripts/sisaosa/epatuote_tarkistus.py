# Independent check of the reduced E, tau on closed twisted solutions with a graded grid near the rim,
# plus the sup of int K for the product limit, and the two-ended holomorphic curve by quadrature.
import numpy as np
from scipy.optimize import brentq
from scipy.integrate import trapezoid, quad, solve_ivp
from epatuote_lib import *

def shoot(mu, b0, Lam, dense=False, rtol=1e-9):
    q = Par(Lam, mu)
    ev = lambda s,u,q: u[1]-np.pi/2
    ev.terminal = True
    sol = integrate(b0, q, 400.0, s0=1e-3, events=ev, rtol=rtol, atol=rtol/10, dense=dense)
    if sol.status != 1: return None, sol
    return np.cos(sol.y_events[0][0][2]), sol

print("== closed twisted solutions: reduced versus direct ==")
for Lam, eps, br in [(0.1, 0.5, (-0.42,-0.32)), (0.1, 0.7, (-0.8,-0.6)), (0.01, 0.7, (-0.06,-0.045)), (0.01, 0.9, (-0.14,-0.10))]:
    b0 = np.pi/2-eps
    mu = brentq(lambda m: shoot(m, b0, Lam, rtol=1e-11)[0], br[0], br[1], xtol=1e-12)
    _, sol = shoot(mu, b0, Lam, dense=True, rtol=1e-12)
    # extend solution slightly past mid by even reflection is unnecessary: integrate past mid
    q = Par(Lam, mu)
    send = sol.t_events[0][0]
    k = np.sqrt(-mu)
    u = sol.y_events[0][0]
    bulk = 2*u[3]*2*Lam + 2*u[4]
    E_red, tau_red = bulk-4, bulk-4+2*(-mu)*2*u[5]
    # rerun without terminal event, dense through the rim
    sol2 = integrate(b0, q, send*1.5, s0=1e-3, rtol=1e-12, atol=1e-13, dense=True)
    # graded grid: clustered at the rim
    t = np.linspace(0, 1, 5001)
    ss = 0.002 + (send-0.002)*(1-(1-t)**3)
    h = 2e-4
    d = direct_check(sol2, ss, 0.0, k, q, h=h)
    Ptt = np.array([r['P']*(Lam*r['gtt']-r['Gtt']) for r in d])
    Pzz = np.array([r['P']*(Lam*r['gzz']-r['Gzz']) for r in d])
    bmid = sol2.sol(send)
    print(f" Lam={Lam} eps={eps} mu={mu:.7f} rim beta'={rhs(send,sol2.sol(send),q)[2]:.2f}  reduced 8GE={E_red:.5f} 8Gtau={tau_red:.5f}   direct 8GE={4*trapezoid(Ptt,ss):.5f} 8Gtau={-4*trapezoid(Pzz,ss):.5f}  max res={max(r['res'] for r in d):.1e}", flush=True)

print("\n== product limit of the lump: sphere part, sup over r of int K ==")
for lam in [0.1, 0.01, 0.001, 1e-4]:
    F2 = lambda r: 1 + 4*lam**2/(lam**2 + r**2)**2
    F = lambda r: np.sqrt(F2(r))
    rs = np.logspace(np.log10(lam)-2, 2, 20001)
    Prs = rs*F(rs)
    dP = np.gradient(Prs, rs)/F(rs)
    iK = 2*np.pi*(1-dP)
    i = np.argmax(iK)
    a = sum(quad(lambda r: 2*np.pi*r*F2(r), x0, x1, limit=400)[0] for x0,x1 in [(0,lam),(lam,rs[i])])
    print(f" lam={lam:8.4f} r_at_sup={rs[i]:.5f} sup int K/(4pi)={iK[i]/(4*np.pi):.6f}  area inside/(4pi)={a/(4*np.pi):.6f}  8G T_core at Lam=0.01: {0.01*a/np.pi - iK[i]/np.pi:.5f} (product {4*0.01-4:.5f})")

print("\n== two-ended holomorphic curve w = A(xi - 1/xi), outside the axisymmetric ansatz ==")
for A in [0.3, 1.0]:
    # metric e^{2 sig}|dxi|^2 with e^{2 sig} = |w'|^2 + 4/(1+|xi|^2)^2
    def e2s(x, y):
        z = x+1j*y
        return np.abs(A*(1+1/z**2))**2 + 4/(1+np.abs(z)**2)**2
    L = 200.0
    rr = np.exp(np.linspace(-np.log(L), np.log(L), 2401))
    ph = np.linspace(0, 2*np.pi, 721)[:-1]
    R_, Ph = np.meshgrid(rr, ph, indexing='ij')
    X, Y = R_*np.cos(Ph), R_*np.sin(Ph)
    sg = 0.5*np.log(e2s(X, Y))
    # flux of grad sigma through the two circles
    dr1 = (sg[-1]-sg[-2])/(rr[-1]-rr[-2])
    dr0 = (sg[1]-sg[0])/(rr[1]-rr[0])
    flux = np.mean(dr1)*2*np.pi*rr[-1] - np.mean(dr0)*2*np.pi*rr[0]
    print(f" A={A}: int K dA = -flux = {-flux/(4*np.pi):.5f} * 4 pi  (expected -1)")
    # area of S^2 part from pullback: integrate 4/(1+|xi|^2)^2 over xi plane = 4 pi exactly
print(" CP1 degree 1, two planar ends: 8GT_rel = 4 Lam + 4, i.e. T = Lam R^2/(8G) + 1/(2G)")

print("\n== null twist momentum on the lump versus cutoff: 8G p = kap^2 * c ==")
for Lam in [0.01, 1e-4]:
  for lam in [0.3, 1.0, 5.0]:
    q = Par(Lam, 0.0)
    b0 = np.arctan2(2.0, lam)
    vals = []
    for rmax in [50.0, 500.0]:
        ev = lambda s,u,q: u[0]-rmax
        ev.terminal = True
        sol = integrate(b0, q, 1e5, s0=1e-3*min(lam,1), events=ev, rtol=1e-10, atol=1e-11)
        # with mu=0, E = L - 2 om^2 d_mu L, so 8G p = -2 kap^2 int dmu
        vals.append(-2*sol.y[5,-1])
    print(f" Lam={Lam} lam={lam}: c(rmax=50)={vals[0]:.5f}, c(rmax=500)={vals[1]:.5f}")
