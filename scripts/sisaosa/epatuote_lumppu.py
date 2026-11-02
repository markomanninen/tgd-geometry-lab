# Twisted localized lumps (mu<0): direct verification and existence map.
import numpy as np, sys
from scipy.special import k1
from scipy.integrate import trapezoid, simpson
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
    sol = integrate(b0, q, 1e6, s0=1e-3, events=[ev_over,ev_turn,ev_r,ev_back,ev_psi], rtol=rtol, atol=rtol/10, dense=dense)
    names = ['over','under','rmax','back','psi0']
    for i,nm in enumerate(names):
        if len(sol.t_events[i]): return nm, sol
    return 'fail', sol

def thresholds(Lam, mu, nb=60):
    q = Par(Lam, mu)
    rmax = 14.0/np.sqrt(-mu)
    bs = np.linspace(0.01, 1.55, nb)
    oc = [outcome(b, q, rmax, rtol=1e-8)[0] for b in bs]
    tr = [i for i in range(len(bs)-1) if {oc[i],oc[i+1]}=={'under','over'}]
    out = []
    for i in tr[:3]:
        a, c = bs[i], bs[i+1]
        oa = oc[i]
        for _ in range(46):
            m = 0.5*(a+c)
            if outcome(m, q, rmax)[0] == oa: a = m
            else: c = m
        out.append(a)
    return q, rmax, out, {k: oc.count(k) for k in set(oc)}

def report(a, q, rmax):
    nm, sol = outcome(a, q, rmax, dense=True, rtol=1e-11)
    y = sol.y[1]; x = sol.y[0]
    j = np.argmax(y)
    psi = np.array([ (lambda v: v[0]+v[6])(f_all(x[i],y[i],sol.y[2,i],q)) for i in range(0,j,max(1,j//400))])
    h = 1e-5*sol.t[j]
    Pp = (PP(*sol.sol(sol.t[j])[:2],q)-PP(*sol.sol(sol.t[j]-h)[:2],q))/h
    A, M, dm = 2*q.Lam*sol.y[3,j], sol.y[4,j], sol.y[5,j]
    E = A + M - q.Lam*x[j]**2 + 2*Pp - 2
    tau = E + 2*(-q.mu)*dm
    return sol, j, E, tau, M, psi.min(), x[j]

mode = sys.argv[1]
if mode == 'direct':
    print("Direct G^{ab} verification of twisted lumps")
    for Lam, mu in [(0.01,-0.01),(0.001,-0.001)]:
        q, rmax, bsol, summ = thresholds(Lam, mu, 77)
        k = np.sqrt(-mu)
        for a in bsol:
            sol, j, E, tau, M, psimin, xc = report(a, q, rmax)
            # integrate only to where delta is still resolved, plane subtracted at that rho
            send = sol.t[j]
            nm = 9000
            t = np.linspace(0,1,nm)
            ss = 0.002*(send/0.002)**t
            hs = 2e-4
            ss = ss[(ss < send-1.0)]
            d = direct_check(sol, ss, 0.0, k, q, h=hs)
            # plane subtracted pointwise, so no large cancellation at the end
            rp = np.array([np.cos(sol.sol(sv)[2]) for sv in ss])
            xs = np.array([r['x'] for r in d])
            plane = 2*Lam*xs*rp
            Ptt = np.array([2*r['P']*(Lam*r['gtt']-r['Gtt']) for r in d]) - plane
            Pzz = np.array([-2*r['P']*(Lam*r['gzz']-r['Gzz']) for r in d]) - plane
            rho_e = d[-1]['x']
            Ed = simpson(Ptt, x=ss)
            td = simpson(Pzz, x=ss)
            pick = np.array(d)[np.linspace(50,len(d)-50,6).astype(int)]
            print(f" Lam={Lam} mu={mu} b0={a:.9f} lam_eff={2/np.tan(a):.3f} min Psi={psimin:.3e} rho_c={xc:.2f}")
            print(f"   reduced: 8GE={E:.6f} 8Gtau={tau:.6f} bulk int M={M:.6f}; direct: 8GE={Ed:.6f} 8Gtau={td:.6f} (to rho={rho_e:.1f})")
            print("   res/|G.B| at samples:", " ".join(f"{r['res']:.1e}/{r['gp']:.1e}" for r in pick), flush=True)
elif mode == 'map':
    print("Existence map: pairs of twisted lumps (lam_eff, E/4Lam, tau/4Lam, intM/4Lam)")
    for Lam in [0.04, 0.03, 0.02, 0.015, 0.01, 0.003, 1e-3, 1e-4, 1e-5]:
        for r_ in [0.03, 0.3, 1.0, 3.0]:
            mu = -r_*Lam
            q, rmax, bsol, summ = thresholds(Lam, mu)
            line = f" Lam={Lam:<8} |mu|/Lam={r_:<5}: {summ} "
            for a in bsol:
                sol, j, E, tau, M, psimin, xc = report(a, q, rmax)
                line += f" [lam={2/np.tan(a):.3f} E/4L={E/(4*Lam):.4f} tau/4L={tau/(4*Lam):.4f} M/4L={M/(4*Lam):+.4f} psi_min={psimin:.1e}]"
            print(line, flush=True)
elif mode == 'muplus':
    print("Timelike tail: E grows with the cutoff")
    for Lam, mu, b0 in [(0.25,0.1,0.8),(0.25,0.01,0.8),(0.01,0.01,0.9)]:
        q = Par(Lam, mu)
        ev = lambda s,u,q: u[0]-400.0
        ev.terminal = True
        def ev_psi(s,u,q):
            f,fx,fy,fb,fbx,fby,fbb,P = f_all(u[0],u[1],u[2],q)
            return f+fbb
        ev_psi.terminal = True
        sol = integrate(b0, q, 4000.0, s0=1e-3, events=[ev, ev_psi], rtol=1e-9, atol=1e-10)
        x,y = sol.y[0], sol.y[1]
        rows = []
        for r in [25,50,100,200,399]:
            i = np.searchsorted(x, r)
            if i >= len(x): break
            E = 2*Lam*sol.y[3,i] + sol.y[4,i] - 2*mu*sol.y[5,i] - Lam*x[i]**2
            rows.append(f"rho={x[i]:.0f}: E={E:.4f}")
        d = np.pi-y
        print(f" Lam={Lam} mu={mu} b0={b0}: end rho={x[-1]:.1f} status {sol.status} psi-stop {len(sol.t_events[1])}; "+", ".join(rows))
    print("Curves that hit the signature change P=0, mu>1")
    for Lam, mu, b0 in [(0.01,2.0,0.3),(0.01,2.0,1.2),(0.01,5.0,0.6),(0.25,3.0,0.5)]:
        q = Par(Lam, mu)
        def ev_P(s,u,q):
            return u[0]**2*(1-q.mu*np.sin(u[1])**2)+np.sin(u[1])**2-1e-9
        ev_P.terminal = True
        def ev_psi(s,u,q):
            f,fx,fy,fb,fbx,fby,fbb,P = f_all(u[0],u[1],u[2],q)
            return f+fbb
        ev_psi.terminal = True
        sol = integrate(b0, q, 200.0, s0=1e-3, events=[ev_P, ev_psi], rtol=1e-8, atol=1e-9)
        u = sol.y[:,-1]
        print(f" Lam={Lam} mu={mu} b0={b0}: rho={u[0]:.4f} Th={u[1]:.4f} mu W={mu*np.sin(u[1])**2:.4f} P^2={u[0]**2*(1-mu*np.sin(u[1])**2)+np.sin(u[1])**2:.3e} stop P0={len(sol.t_events[0])} psi0={len(sol.t_events[1])} partial 2Lam int P={2*Lam*u[3]:.4f} int M={u[4]:.4f} beta={u[2]:.3f} s={sol.t[-1]:.3f}")
