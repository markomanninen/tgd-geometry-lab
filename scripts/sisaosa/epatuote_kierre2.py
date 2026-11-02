# Continue the closed spacelike-twist branch with mu as the parameter, and verify E, tau by direct G^{ab}.
import numpy as np
from scipy.optimize import brentq
from scipy.integrate import trapezoid
from epatuote_lib import *

def shoot(mu, b0, Lam, dense=False):
    q = Par(Lam, mu)
    ev = lambda s,u,q: u[1]-np.pi/2
    ev.terminal = True
    ev2 = lambda s,u,q: u[0]
    ev2.terminal = True; ev2.direction = -1
    sol = integrate(b0, q, 400.0, s0=1e-3, events=[ev, ev2], rtol=1e-9, atol=1e-10, dense=dense)
    if sol.status != 1 or len(sol.t_events[0]) == 0:
        return None, sol
    return np.cos(sol.y_events[0][0][2]), sol

def energy(sol, mu, Lam):
    u = sol.y_events[0][0]
    bulk = 2*u[3]*2*Lam + 2*u[4]
    return bulk-4, bulk-4+2*(-mu)*2*u[5], u[0], 2*u[3]*2*Lam, 2*u[4]

for Lam in [0.5, 0.01]:
    print(f"\nLam={Lam}, scan mu at fixed mu, all b0 roots on a grid")
    print("    mu       b0      rho_max   8G E      8G tau    area     M")
    for mu in -np.array([1.0,3,10,30,100,300,1000,3000])*(1.0 if Lam==0.5 else 0.3):
        bs = np.linspace(0.02, np.pi/2-0.002, 90)
        vals = [shoot(mu, b, Lam)[0] for b in bs]
        nroot = 0
        for i in range(len(bs)-1):
            a, c = vals[i], vals[i+1]
            if a is None or c is None or a*c > 0: continue
            r = brentq(lambda b: shoot(mu, b, Lam)[0], bs[i], bs[i+1], xtol=1e-9)
            _, sol = shoot(mu, r, Lam)
            E, t, rm, A, M = energy(sol, mu, Lam)
            print(f"  {mu:9.3f} {r:8.5f} {rm:8.4f} {E:10.4f} {t:10.4f} {A:9.4f} {M:9.4f}", flush=True)
            nroot += 1
        if nroot == 0:
            print(f"  {mu:9.3f}  no symmetric closed solution on the grid")

print("\nDirect check on one closed solution, Lam=0.01, b0=pi/2-0.9")
Lam = 0.01; b0 = np.pi/2-0.9
mu = brentq(lambda m: shoot(m, b0, Lam)[0], -0.14, -0.10, xtol=1e-11)
_, sol = shoot(mu, b0, Lam, dense=True)
sol.sol = sol.sol
q = Par(Lam, mu)
k = np.sqrt(-mu)
send = sol.t_events[0][0]
E, t, rm, A, M = energy(sol, mu, Lam)
print(f" mu={mu:.8f} k={k:.6f} s_mid={send:.5f}; reduced: 8G E={E:.6f}, 8G tau={t:.6f}")
pts = np.linspace(0.02, send-0.02, 7)
for r in direct_check(sol, pts, 0.0, k, q, h=1e-3):
    print(f"  s={r['s']:.3f} rho={r['x']:.4f} Th={r['y']:.4f} R={r['R']:+.4e} res={r['res']:.1e} |G.B|={r['gp']:.2e} |Lam g.B part|~ tang={r['tang']:.1e}")
ss = np.linspace(2e-3, send-2e-3, 1601)
d = direct_check(sol, ss, 0.0, k, q, h=1e-3)
Ptt = np.array([r['P']*(Lam*r['gtt']-r['Gtt']) for r in d])
Pzz = np.array([r['P']*(Lam*r['gzz']-r['Gzz']) for r in d])
print(f" direct, full surface: 8G E = {2*2*trapezoid(Ptt,ss):.6f}, 8G tau = {-2*2*trapezoid(Pzz,ss):.6f}")
