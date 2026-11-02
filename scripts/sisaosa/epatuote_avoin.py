# Open surfaces with mu != 0: start at the regular axis, follow the curve to large rho.
# Reports the fate of the curve and whether a localized tail exists.
import numpy as np
from epatuote_lib import *

def fate(b0, Lam, mu, rmax=60.0):
    q = Par(Lam, mu)
    ev1 = lambda s,u,q: u[0]-rmax
    ev1.terminal = True
    ev2 = lambda s,u,q: u[0]
    ev2.terminal = True; ev2.direction = -1
    ev3 = lambda s,u,q: u[1]-np.pi
    ev3.terminal = True
    def ev4(s,u,q):
        f, fx, fy, fb, fbx, fby, fbb, P = f_all(u[0],u[1],u[2],q)
        return (f+fbb)/(abs(2*q.Lam*P)+abs(fbb)+1e-300) 
    ev4.terminal = True
    def ev5(s,u,q):
        return u[0]**2*(1-mu*np.sin(u[1])**2)+np.sin(u[1])**2
    ev5.terminal = True
    sol = integrate(b0, q, 4000.0, s0=1e-3, events=[ev1,ev2,ev3,ev4,ev5], rtol=1e-8, atol=1e-9)
    names = ['rmax','back-to-rho0','reach-pi','Psi=0','P=0','none']
    idx = 5
    for i in range(5):
        if len(sol.t_events[i]): idx = i
    return names[idx], sol

for Lam in [0.25, 0.01, 0.001]:
    for mu in [-1.0, -0.1, -0.01, 0.01, 0.1, 1.0, 2.0]:
        res = {}
        ex = {}
        for b0 in np.linspace(0.05, np.pi/2-0.02, 40):
            nm, sol = fate(b0, Lam, mu)
            res[nm] = res.get(nm, 0)+1
            ex.setdefault(nm, (round(b0,3), round(sol.y[0,-1],3), round(sol.y[1,-1],3)))
        print(f"Lam={Lam:6.3f} mu={mu:6.2f}: {res}   examples (b0,rho_end,Th_end) {ex}", flush=True)

print("\nTail test, timelike and spacelike, Lam=0.01, b0=1.1:")
for mu in [0.1, -0.1]:
    q = Par(0.01, mu)
    ev1 = lambda s,u,q: u[0]-120.0
    ev1.terminal=True
    sol = integrate(1.1, q, 1000.0, s0=1e-3, events=ev1, rtol=1e-8, atol=1e-9)
    idx = np.searchsorted(sol.y[0], [5,10,20,40,80,119])
    print(f" mu={mu}: rho,Th:", [(round(sol.y[0,i],1), round(sol.y[1,i],4)) for i in idx if i<sol.y.shape[1]], " status", sol.status)
    # energy excess growth: 8G E for mu>0 omega^2=mu: L - 2 omega^2 d_mu L, minus plane; for mu<0: L
    area = 2*0.01*sol.y[3]; M = sol.y[4]; dm = sol.y[5]
    w2 = max(mu,0.0)
    Erel = area + M - 2*w2*dm - 0.01*sol.y[0]**2
    print("   8G E_rel(no boundary term):", [round(Erel[i],4) for i in idx if i<sol.y.shape[1]])
