# Closed cross-section with spacelike twist: mu<0, curve from (0,0) to (0,pi), symmetric about Theta=pi/2.
# mu is the eigenvalue found by requiring rho'=0 at Theta=pi/2.
import numpy as np, sys
from scipy.optimize import brentq
from epatuote_lib import *

def shoot(mu, b0, Lam):
    q = Par(Lam, mu)
    ev = lambda s,u,q: u[1]-np.pi/2
    ev.terminal = True
    ev2 = lambda s,u,q: u[0]
    ev2.terminal = True; ev2.direction = -1
    sol = integrate(b0, q, 200.0, s0=1e-3, events=[ev, ev2], rtol=1e-9, atol=1e-10)
    if sol.status != 1 or len(sol.t_events[0]) == 0:
        return None, sol
    return np.cos(sol.y_events[0][0][2]), sol

def energy(sol, mu, Lam):
    u = sol.y_events[0][0]
    A2, M2, dm2 = 2*u[3]*2*Lam, 2*u[4], 2*u[5]
    # 8G E = bulk - 4; 8G tau = E + 2 k^2 d_mu L, with k^2 = -mu, omega = 0
    bulk = A2 + M2
    return dict(Area=A2, M=M2, E=bulk-4, tau=bulk-4 + 2*(-mu)*dm2, rmax=u[0], s=sol.t_events[0][0])

for Lam in [0.5, 0.1, 0.01, 0.001]:
    mu0 = -2*Lam/(1-Lam)
    print(f"\nLam={Lam}  (Lam R^2 = {4*Lam})  linear prediction mu={mu0:.6f}   product 8GT={4*Lam-4:.4f}")
    print("  eps=pi/2-b0  mu          mu/mu0     rho_max    8G E      8G tau    area/(4 Lam)  bulk M")
    prev = mu0
    for eps in [1e-2, 0.05, 0.1, 0.2, 0.35, 0.5, 0.7, 0.9, 1.1, 1.3, 1.45, 1.52, 1.55]:
        b0 = np.pi/2 - eps
        found = None
        # bracket around the previous eigenvalue
        for fac in [1.02, 1.1, 1.3, 1.7, 2.5, 4, 8, 16, 32, 64, 128]:
            lo, hi = prev/fac, prev*fac
            a, _ = shoot(lo, b0, Lam); c, _ = shoot(hi, b0, Lam)
            if a is None or c is None: continue
            if a*c < 0:
                found = brentq(lambda m: shoot(m, b0, Lam)[0], lo, hi, xtol=1e-9*abs(prev), rtol=1e-9, maxiter=60)
                break
        if found is None:
            print(f"  {eps:6.3f}  no bracket (prev mu={prev:.5f})")
            continue
        prev = found
        _, sol = shoot(found, b0, Lam)
        e = energy(sol, found, Lam)
        print(f"  {eps:6.3f} {found:11.6f} {found/mu0:8.4f} {e['rmax']:9.4f} {e['E']:9.5f} {e['tau']:9.5f} {e['Area']/(4*Lam):9.4f} {e['M']:9.5f}", flush=True)
