# (a) spacelike twisted lumps: bisect the initial direction between undershoot and overshoot of Theta=pi.
# (b) timelike closed search with mu>0.
import numpy as np
from scipy.special import k1
from scipy.integrate import trapezoid
from epatuote_lib import *

def outcome(b0, q, rmax, dense=False, rtol=1e-10):
    ev_over = lambda s,u,q: u[1]-np.pi
    ev_over.terminal = True
    ev_turn = lambda s,u,q: np.sin(u[2])
    ev_turn.terminal = True; ev_turn.direction = -1
    ev_r = lambda s,u,q: u[0]-rmax
    ev_r.terminal = True
    ev_back = lambda s,u,q: u[0]
    ev_back.terminal = True; ev_back.direction = -1
    def ev_psi(s,u,q):
        f,fx,fy,fb,fbx,fby,fbb,P = f_all(u[0],u[1],u[2],q)
        return f+fbb
    ev_psi.terminal = True
    def ev_P(s,u,q):
        return u[0]**2*(1-q.mu*np.sin(u[1])**2)+np.sin(u[1])**2-1e-9
    ev_P.terminal = True
    sol = integrate(b0, q, 1e4, s0=1e-3, events=[ev_over,ev_turn,ev_r,ev_back,ev_psi,ev_P], rtol=rtol, atol=rtol/10, dense=dense)
    names = ['over','under','rmax','back','psi0','P0']
    for i,nm in enumerate(names):
        if len(sol.t_events[i]): return nm, sol
    return 'fail', sol

print("(a) spacelike: outcome map and bisection")
for Lam, mu in [(0.01,-0.01),(0.01,-0.003),(0.01,-0.03),(0.003,-0.003),(0.001,-0.001),(0.001,-0.003),(0.001,-0.01),(0.1,-0.03),(0.03,-0.03)]:
    q = Par(Lam, mu)
    rmax = 14.0/np.sqrt(-mu)
    bs = np.linspace(0.02, 1.55, 77)
    oc = [outcome(b, q, rmax, rtol=1e-8)[0] for b in bs]
    # find transitions under<->over
    tr = [i for i in range(len(bs)-1) if {oc[i],oc[i+1]}=={'under','over'}]
    summ = {k: oc.count(k) for k in set(oc)}
    print(f" Lam={Lam} mu={mu}: {summ}  transitions at b0 ~ {[round(bs[i],3) for i in tr]}", flush=True)
    for i in tr[:3]:
        a, c = bs[i], bs[i+1]
        oa = oc[i]
        for _ in range(46):
            m = 0.5*(a+c)
            o = outcome(m, q, rmax)[0]
            if o == oa: a = m
            else: c = m
        nm, sol = outcome(a, q, rmax, dense=True)
        x, y = sol.y[0], sol.y[1]
        # closest approach to pi
        j = np.argmax(y)
        rho_c, dmin = x[j], np.pi-y[j]
        # tail fit between delta=1e-1 and delta=1e-3 region
        mask = (np.pi-y[:j] < 0.05) & (np.pi-y[:j] > 3e-5)
        ka = np.sqrt(-mu)
        if mask.sum()>5:
            ratio = (np.pi-y[:j])[mask]/k1(ka*x[:j][mask])
            spread = ratio.max()/ratio.min()
        else:
            spread = np.nan
        h = 1e-5*sol.t[j]
        Pp = (PP(*sol.sol(sol.t[j])[:2],q)-PP(*sol.sol(sol.t[j]-h)[:2],q))/h
        A, M, dm = 2*Lam*sol.y[3,j], sol.y[4,j], sol.y[5,j]
        E = A + M - Lam*rho_c**2 + 2*Pp - 2
        tau = E + 2*(-mu)*dm
        print(f"   b0*={a:.10f} lam_eff={2/np.tan(a):.4f} stop={nm} rho_c={rho_c:.3f} dmin={dmin:.2e} tail/K1 spread={spread:.3f}  8GE={E:.6f} 8Gtau={tau:.6f} area_exc/(4Lam)={(A-Lam*rho_c**2)/(4*Lam):.4f} M={M:.6f} 2P'-2={2*Pp-2:.2e}   compare 4Lam={4*Lam}", flush=True)

print("\n(b) timelike: symmetric closure search, mu>0, reports crossings of Theta=pi/2 and fates")
for Lam in [0.25, 0.01]:
    for mu in [0.5, 1.0, 1.1, 1.5, 2.0, 3.0, 5.0, 10.0]:
        q = Par(Lam, mu)
        bs = np.linspace(0.03, 1.55, 77)
        res = {}
        val = []
        for b in bs:
            ev_mid = lambda s,u,q: u[1]-np.pi/2
            ev_mid.terminal = True
            def ev_P(s,u,q):
                return u[0]**2*(1-q.mu*np.sin(u[1])**2)+np.sin(u[1])**2-1e-9
            ev_P.terminal = True
            def ev_psi(s,u,q):
                f,fx,fy,fb,fbx,fby,fbb,P = f_all(u[0],u[1],u[2],q)
                return f+fbb
            ev_psi.terminal = True
            ev_back = lambda s,u,q: u[0]
            ev_back.terminal = True; ev_back.direction=-1
            ev_r = lambda s,u,q: u[0]-40
            ev_r.terminal = True
            sol = integrate(b, q, 400.0, s0=1e-3, events=[ev_mid, ev_P, ev_psi, ev_back, ev_r], rtol=1e-8, atol=1e-9)
            lab = ['mid','P0','psi0','back','rmax'][[len(e)>0 for e in sol.t_events].index(True)] if any(len(e)>0 for e in sol.t_events) else 'fail'
            res[lab] = res.get(lab,0)+1
            val.append(np.cos(sol.y_events[0][0][2]) if lab=='mid' else np.nan)
        val = np.array(val)
        sc = [round(bs[i],3) for i in range(len(bs)-1) if np.isfinite(val[i]) and np.isfinite(val[i+1]) and val[i]*val[i+1]<0]
        print(f" Lam={Lam} mu={mu}: {res}  symmetric-closure sign changes at b0~{sc}", flush=True)
