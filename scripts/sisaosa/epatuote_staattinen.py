# Static and null sectors (mu = 0). Exact solutions and shooting agree?
import numpy as np, sys
from scipy.integrate import quad, trapezoid
from epatuote_lib import *

def lump_exact(lam):
    F2 = lambda r: 1 + 4*lam**2/(lam**2 + r**2)**2
    return F2

print("== 1. Shooting from the regular axis, mu=0, compare with rho cot(Theta/2) = lam, exact holomorphic xi = w/lam ==")
q = Par(0.01, 0.0)
print(" lam  beta0     max|rho cot(Th/2)-lam|/lam (up to rho=50)  y_end     8GT_rel(area)/Lam   int K dA/(4pi)")
for lam in [0.05, 0.2, 1.0, 3.0, 20.0]:
    b0 = np.arctan2(2.0, lam)
    ev = lambda s,u,q: u[0]-200.0*max(lam,1)
    ev.terminal = True
    sol = integrate(b0, q, 2e5, s0=1e-3*min(lam,1), events=ev, dense=True)
    x, y, b = sol.y[:3]
    mask = (y < np.pi-1e-3)&(sol.t>1e-2*min(lam,1))
    dev = np.max(np.abs(x[mask]/np.tan(y[mask]/2) - lam))/lam
    # area excess over the plane, in units where 8GT = int ds 2 Lam P
    Pend = PP(x[-1], y[-1], q)
    area = sol.y[3,-1]
    exc = area - x[-1]**2/2
    # int K dA = 2 pi (1 - P'/N at the end); P'/N = dP/ds
    h=1e-4*sol.t[-1]
    dP = (PP(*sol.sol(sol.t[-1])[:2],q)-PP(*sol.sol(sol.t[-1]-h)[:2],q))/h
    print(f" {lam:5.2f} {b0:7.4f}  {dev:10.2e}  {y[-1]:9.6f}  {2*exc:10.6f}  {(1-dP)/2:10.2e}")

print("\n== 2. Exact lump integrals, by quadrature ==")
print(" lam   excess area/(4 pi)    int K dA [0,inf)/(4pi)   K_min     K_max   rho_neck  P_neck")
for lam in [10, 1, 0.1, 0.01, 0.001]:
    F2 = lambda r: 1 + 4*lam**2/(lam**2 + r**2)**2
    F = lambda r: np.sqrt(F2(r))
    exc = sum(quad(lambda r: 2*np.pi*r*(F2(r)-1), a, b, limit=400)[0] for a,b in [(0,lam),(lam,10*lam),(10*lam,np.inf)])
    # K from conformal factor sigma = ln F
    def K(r, e=1e-5):
        rr=max(r,1e-9)*np.array([1-e,1,1+e])
        s=0.5*np.log(1+4*lam**2/(lam**2+rr**2)**2)
        d1=(s[2]-s[0])/(rr[2]-rr[0]); d2=((s[2]-s[1])/(rr[2]-rr[1])-(s[1]-s[0])/(rr[1]-rr[0]))/((rr[2]-rr[0])/2)
        return -(d2+d1/rr[1])/F2(rr[1])
    rs = np.logspace(np.log10(lam)-3, np.log10(lam)+6, 40001)
    Ks = np.array([K(r) for r in rs])
    Fs = F(rs)
    Ptot = rs*Fs
    # neck = minimum of circle radius P beyond the maximum (only for thin lumps)
    i_max = np.argmax(Ptot[:len(rs)//2]) if lam<0.3 else None
    dKint = None
    # analytic boundary form: int_{r<rc} K dA = 2 pi (1 - d(rF)/(F dr))
    def intK(rc):
        h=rc*1e-5
        return 2*np.pi*(1-((rc+h)*F(rc+h)-(rc-h)*F(rc-h))/(2*h)/F(rc))
    tot = intK(rs[-1])
    if lam<0.3:
        dP = np.gradient(Ptot, rs)
        neck = rs[np.where((dP[:-1]<0)&(dP[1:]>0))[0][0]]
        print(f" {lam:7.3f} {exc/(4*np.pi):12.8f} {tot/(4*np.pi):12.3e} {Ks.min():11.3f} {Ks.max():9.4f} {neck:9.5f} {neck*F(neck):9.5f}   int K up to neck/(4pi)={intK(neck)/(4*np.pi):.6f}, area up to neck/(4pi)={quad(lambda r:2*np.pi*r*F2(r),0,neck,limit=400)[0]/(4*np.pi):.6f}")
    else:
        print(f" {lam:7.3f} {exc/(4*np.pi):12.8f} {tot/(4*np.pi):12.3e} {Ks.min():11.5f} {Ks.max():9.5f}")

print("\n== 3. Two-ended holomorphic curve rho = -2A cot Theta, degree 1 on CP1, two planar ends ==")
q = Par(0.01, 0.0)
print(" A   dev from curve   8GT_rel/ (4 Lam) part  bracket part")
for A in [0.1, 0.5, 2.0]:
    # start at rho=0, Theta=pi/2 with slope drho/dTheta = 2A
    b0 = np.arctan2(1.0, 2*A)
    ev = lambda s,u,q: u[0]-300.0*max(A,1)
    ev.terminal=True
    u0 = [0.0, np.pi/2, b0, 0,0,0]
    sol = solve_ivp(rhs,[0,5e4],u0,args=(q,),method='DOP853',rtol=1e-10,atol=1e-11,events=ev,dense_output=True)
    x,y=sol.y[:2]
    mask=y<np.pi-1e-3
    dev=np.max(np.abs(x[mask]+2*A/np.tan(y[mask])))/ (2*A)
    Ph=sol.y[3,-1]-x[-1]**2/2   # half surface area excess/(2 pi), one side
    h=1e-4*sol.t[-1]
    dP=(PP(*sol.sol(sol.t[-1])[:2],q)-PP(*sol.sol(sol.t[-1]-h)[:2],q))/h
    # int K dA over whole annulus: both sides symmetric, at rho=0 P'=0
    intK = -2*2*np.pi*dP
    print(f" {A:4.1f} {dev:10.2e}  excess area/(4pi) = {2*2*np.pi*Ph/(4*np.pi):.6f}, int K dA/(4pi) = {intK/(4*np.pi):.6f}")

print("\n== 4. Direct check on the static lump, lam=1, Lam=0.01: metric -> G^{ab}, then field equation ==")
q = Par(0.01, 0.0)
sol = integrate(np.arctan2(2.0,1.0), q, 60.0, s0=1e-3, dense=True)
pts = np.linspace(0.2, 30.0, 9)
L8G = 0
for r in direct_check(sol, pts, 0.0, 0.0, q):
    F2 = 1+4/(1+r['x']**2)**2
    print(f" s={r['s']:7.3f} rho={r['x']:8.4f} Th={r['y']:7.4f} R={r['R']:+.5e} Gtt={r['Gtt']:+.5e} (Gtt+R/2={r['Gtt']+r['R']/2:+.1e}) res={r['res']:.1e} |G.B|={r['gp']:.1e} tang={r['tang']:.1e}")

print("\n== 5. Null twist: same curve, omega=k=kap (mu=0), Lam=0.01, lam=1 ==")
for kap in [0.3, 1.0, 3.0]:
    q = Par(0.01, 0.0)
    rows = direct_check(sol, pts[:4], kap, kap, q)
    print(f" kap={kap}: ", " ".join(f"res={r['res']:.1e}/G.B={r['gp']:.1e}" for r in rows))
    # energy and momentum per length from direct G^{ab}, Lam part relative to plane
    ss = np.linspace(1e-2, 58, 6001)
    d = direct_check(sol, ss, kap, kap, q)
    Ett = np.array([2*r['P']*(q.Lam*r['gtt'] - r['Gtt']) for r in d])
    Ezz = np.array([2*r['P']*(q.Lam*r['gzz'] - r['Gzz']) for r in d])
    Etz = np.array([2*r['P']*(q.Lam*r['gtz'] - r['Gtz']) for r in d])
    plane = np.array([2*r['x'] for r in d])*(q.Lam)*np.gradient([r['x'] for r in d], ss)
    I_tt = trapezoid(Ett-plane, ss)
    I_zz = trapezoid(Ezz+plane, ss)
    I_tz = trapezoid(Etz, ss)
    print(f"   8G E_rel={I_tt:.6f}  8G(P^zz)_rel={I_zz:.6f}  8G P^tz={I_tz:.6f}  E+P^zz={I_tt+I_zz:.6f} (2*static value 4Lam*... ) invariant E^2-p^2 sqrt: {np.sqrt(abs(I_tt**2-I_tz**2)):.6f}")
