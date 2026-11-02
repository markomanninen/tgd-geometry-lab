# Direct curvature from exact metric jets: the generic Christoffel-Ricci routine gets g, g', g'' from the
# embedding functions (rho, Theta, beta, beta'), so no differentiation of interpolated data is needed.
import numpy as np, sys
from scipy.integrate import simpson
from scipy.optimize import brentq
sys.argv = ['x','none']
exec(open('epatuote_lumppu.py').read().split("mode = sys.argv[1]")[0])

def G_from_jets(g, dg, ddg):
    S = 2
    ginv = np.linalg.inv(g)
    dginv = -ginv @ dg @ ginv
    D = np.zeros((4,4,4)); D[S] = dg
    DD = np.zeros((4,4,4)); DD[S] = ddg
    low = np.zeros((4,4,4)); dlow = np.zeros((4,4,4))
    for d in range(4):
        for b in range(4):
            for c in range(4):
                low[d,b,c] = 0.5*(D[c,d,b]+D[b,d,c]-D[d,b,c])
                dlow[d,b,c] = 0.5*(DD[c,d,b]+DD[b,d,c]-DD[d,b,c])
    Gam = np.einsum('ad,dbc->abc', ginv, low)
    dGam = np.einsum('ad,dbc->abc', dginv, low) + np.einsum('ad,dbc->abc', ginv, dlow)
    Ric = np.zeros((4,4))
    for b in range(4):
        for d in range(4):
            t1 = dGam[S,b,d]
            t2 = sum(dGam[a,b,a] for a in range(4)) if d==S else 0.0
            t3 = sum(Gam[a,a,e]*Gam[e,b,d] for a in range(4) for e in range(4))
            t4 = sum(Gam[a,d,e]*Gam[e,b,a] for a in range(4) for e in range(4))
            Ric[b,d] = t1-t2+t3-t4
    Rs = np.sum(ginv*Ric)
    return ginv @ (Ric-0.5*Rs*g) @ ginv, ginv, Rs

def jets(u, q, om, k):
    x,y,b = u[:3]
    db = rhs(0.0, u, q)[2]
    x1,y1 = np.cos(b), np.sin(b)
    x2,y2 = -np.sin(b)*db, np.cos(b)*db
    m,n = q.m,q.n
    p,p1,p2 = m**2*x**2, 2*m**2*x*x1, 2*m**2*(x1**2+x*x2)
    W,W1,W2 = np.sin(y)**2, np.sin(2*y)*y1, 2*np.cos(2*y)*y1**2+np.sin(2*y)*y2
    v = np.array([om,k,0.0,n]); vv = np.outer(v,v)
    return np.diag([1.,-1,-1,-p])-W*vv, np.diag([0.,0,0,-p1])-W1*vv, np.diag([0.,0,0,-p2])-W2*vv

print("Twisted lumps: reduced versus direct curvature from exact jets")
for Lam, mu in [(0.01,-0.01),(0.001,-0.001),(1e-4,-1e-4)]:
    q, rmax, bsol, summ = thresholds(Lam, mu, 77)
    k = np.sqrt(-mu)
    for a in bsol:
        sol, j, E, tau, M, psimin, xc = report(a, q, rmax)
        send = sol.t[j]
        ss = 0.002*(send/0.002)**np.linspace(0,1,12001)
        ss = ss[ss<send]
        pt = np.zeros(len(ss)); pz = np.zeros(len(ss))
        for i,sv in enumerate(ss):
            u = sol.sol(sv)
            g,dg,ddg = jets(u,q,0.0,k)
            Gu,gi,Rs = G_from_jets(g,dg,ddg)
            P = PP(u[0],u[1],q)
            plane = 2*Lam*u[0]*np.cos(u[2])
            pt[i] = 2*P*(Lam*gi[0,0]-Gu[0,0])-plane
            pz[i] = -2*P*(Lam*gi[1,1]-Gu[1,1])-plane
        print(f" Lam={Lam} mu={mu} lam={2/np.tan(a):.3f}: reduced 8GE={E:.7f} 8Gtau={tau:.7f}  direct 8GE={simpson(pt,x=ss):.7f} 8Gtau={simpson(pz,x=ss):.7f}", flush=True)

print("\nVirial identity on a closed twisted solution, Lam=0.1, eps=0.7")
def shoot(mu, b0, Lam, dense=False):
    q = Par(Lam, mu)
    ev = lambda s,u,q: u[1]-np.pi/2
    ev.terminal = True
    sol = integrate(b0, q, 400.0, s0=1e-3, events=ev, rtol=1e-11, atol=1e-12, dense=dense)
    return np.cos(sol.y_events[0][0][2]), sol
b0 = np.pi/2-0.7
mu = brentq(lambda m: shoot(m,b0,0.1)[0], -0.8,-0.6, xtol=1e-12)
_, sol = shoot(mu,b0,0.1,True)
send = sol.t_events[0][0]
s = np.linspace(1e-3, send, 40001)
u = sol.sol(s); x,y,b = u[:3]; c,sn = np.cos(b),np.sin(b)
W = np.sin(y)**2; P = np.sqrt(x**2*(1-mu*W)+W)
Mloc = mu*2*x*c*np.sin(2*y)*sn/(2*P)
t1 = 2*0.1*(c**2*P + x**2*(1-mu*W)/P)
t2 = Mloc*(2-c**2-x**2*(1-mu*W)/P**2)
print(f" int term1={simpson(t1,x=s):.6f} int term2={simpson(t2,x=s):.6f} sum={simpson(t1+t2,x=s):.2e}")

print("\nPhysical scale Lam R^2 = 1.76e-6, i.e. Lam/K = 4.4e-7")
Lam = 4.4e-7
for r_ in [0.3, 1.0]:
    q, rmax, bsol, summ = thresholds(Lam, -r_*Lam)
    line = f" |mu|/Lam={r_}: {summ}"
    for a in bsol:
        sol, j, E, tau, M, psimin, xc = report(a, q, rmax)
        line += f" [lam={2/np.tan(a):.3f} E/4L={E/(4*Lam):.4f} tau/4L={tau/(4*Lam):.4f} M/4L={M/(4*Lam):+.4f}]"
    print(line, flush=True)

print("\nPointwise sign of Lam-K on the static lump: K_max lam^2 and K_min lam^2")
for lam in [3, 10, 100, 1000]:
    r = np.logspace(np.log10(lam)-2, np.log10(lam)+2, 6001)
    # exact K = -e^{-2 sig} Lap sig with e^{2 sig} = 1 + 4 lam^2/(lam^2+r^2)^2
    h = 1e-4*r
    sg = lambda t: 0.5*np.log1p(4*lam**2/(lam**2+t**2)**2)
    d2 = (sg(r+h)-2*sg(r)+sg(r-h))/h**2
    d1 = (sg(r+h)-sg(r-h))/(2*h)
    K = -(d2+d1/r)/(1+4*lam**2/(lam**2+r**2)**2)
    print(f" lam={lam}: K_max lam^2={K.max()*lam**2:.4f} at r/lam={r[K.argmax()]/lam:.3f}, K_min lam^2={K.min()*lam**2:.4f}")
