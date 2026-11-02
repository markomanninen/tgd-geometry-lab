#!/usr/bin/env python3
"""Factor 2 in M_gr: Einstein tensor on M^2 x Y^2, Gauss-Bonnet, candidate mass definitions,
lapse variation fixing the Noether coefficient, and connected-sum geometry."""
import sympy as sp
t,z,x,y=sp.symbols('t z x y',real=True)
phi=sp.Function('phi')(x,y)
G_N=sp.symbols('G',positive=True)
coords=[t,z,x,y]
# signature (-,+,+,+); transverse metric e^{2phi}(dx^2+dy^2)
g=sp.diag(-1,1,sp.exp(2*phi),sp.exp(2*phi))
ginv=g.inv()
def christoffel(g,ginv,X):
    n=len(X)
    return [[[sum(ginv[a,d]*(sp.diff(g[d,b],X[c])+sp.diff(g[d,c],X[b])-sp.diff(g[b,c],X[d])) for d in range(n))/2 for c in range(n)] for b in range(n)] for a in range(n)]
def ricci(g,ginv,X):
    n=len(X);Gam=christoffel(g,ginv,X)
    R=sp.zeros(n,n)
    for b in range(n):
        for c in range(n):
            R[b,c]=sum(sp.diff(Gam[a][b][c],X[a])-sp.diff(Gam[a][b][a],X[c]) for a in range(n))+sum(Gam[a][a][d]*Gam[d][b][c]-Gam[a][c][d]*Gam[d][b][a] for a in range(n) for d in range(n))
    return R.applyfunc(sp.simplify)
Ric=ricci(g,ginv,coords)
Rs=sp.simplify(sum(ginv[a,b]*Ric[a,b] for a in range(4) for b in range(4)))
Gd=(Ric-g*Rs/2).applyfunc(sp.simplify)
Gu=(ginv*Gd*ginv).applyfunc(sp.simplify)
K=-sp.exp(-2*phi)*(sp.diff(phi,x,2)+sp.diff(phi,y,2))  # Gaussian curvature
print("R-2K =",sp.simplify(Rs-2*K))
print("G^tt-K =",sp.simplify(Gu[0,0]-K)," G^zz+K =",sp.simplify(Gu[1,1]+K)," G^xx =",Gu[2,2]," G^yy =",Gu[3,3])
print("Tolman rho+sum p (units K/8piG) =",sp.simplify((Gu[0,0]+Gu[1,1]+g[2,2]*Gu[2,2]+g[3,3]*Gu[3,3])/K))
print("R_tt (trace-reversed) =",Ric[0,0], " R_zz =",Ric[1,1])
# Lapse variation: g_tt=-(1+2 eps f(x,y)), static. d/deps of sqrt(-g) R at eps=0
eps=sp.symbols('epsilon');f=sp.Function('f')(x,y)
ge=sp.diag(-(1+2*eps*f),1,sp.exp(2*phi),sp.exp(2*phi))
gi=ge.inv()
Rice=ricci(ge,gi,coords)
Rse=sum(gi[a,a]*Rice[a,a] for a in range(4))
L=sp.sqrt(1+2*eps*f)*sp.exp(2*phi)*Rse
dL=sp.simplify(sp.diff(L,eps).subs(eps,0))
# Expected: sqrt(h)(f R_h) + total derivative -2 sqrt(h) Lap_h f
lap=sp.diff(f,x,2)+sp.diff(f,y,2)
print("d(sqrt g R)/deps - [e^{2phi} f 2K - 2 Lap f] =",sp.simplify(dL-(sp.exp(2*phi)*f*2*K-2*lap)))
print("=> energy density conjugate to lapse = 2K/(16 pi G) = K/(8 pi G) = G^tt/(8 pi G)")
pi=sp.pi
print("\n# Values for closed Y^2, chi=2-2g, int K=2 pi chi")
g_s=sp.symbols('g_genus')
chi=2-2*g_s
for name,val in [("(1/8piG) int G^tt",2*pi*chi/(8*pi*G_N)),("(1/16piG) int R",2*2*pi*chi/(16*pi*G_N)),("(1/16piG) int G^tt",2*pi*chi/(16*pi*G_N)),("(1/16piG) int K",2*pi*chi/(16*pi*G_N))]:
    print(f"{name:24s}=",sp.simplify(val))
print("deficit 8 pi G mu for mu=(1-g)/2G:",sp.simplify(8*pi*G_N*(1-g_s)/(2*G_N)),"  for mu=(1-g)/4G:",sp.simplify(8*pi*G_N*(1-g_s)/(4*G_N)))
# Surfaces of revolution: numeric total curvature for capped cylinder and plane with attached sphere
print("\n# Connected sum check: profile (r(s),z(s)) arclength, K=-r''/r, int K dA=2pi[r'(0)-r'(L)]")
print("hemisphere cap + cylinder: r'(0)=1, r'(L)=0: int K=2pi, mu=1/(4G), deficit 2pi")
print("cone with deficit d: r'(L)=1-d/2pi: int K=d")
print("sphere attached to plane by a neck: r'(0)=1 at far pole, r'(L)=1 on the plane: int K=0, mu=0, deficit 0")
print("  sphere part +4pi - neck -4pi: check numerically")
import math
# Direct Gauss-Bonnet by turning of the tangent: profile angle psi, r'=cos psi, z'=sin psi, K dA=2pi d(sin? ) 
a=1.0;b=0.15;rc=0.6
zc=b+math.sqrt((a+b)**2-rc**2)
# Sphere: from top pole: tangent angle: r'=cos(psi) with psi from 0 (horizontal) going down
# total curvature of a revolution piece = 2pi [cos(psi_start)-cos(psi_end)] 
th=math.atan2(rc,zc-b)            # polar angle from the downward axis to the neck centre
# Sphere from top pole (r'=1) to the junction: r'=cos(pi-th)=-cos(th)
sph=2*math.pi*(1-(-math.cos(th)))
# Neck from junction r'=-cos(th) to the plane r'=1
neck=2*math.pi*(-math.cos(th)-1)
print(f"  sphere piece {sph/math.pi:.4f} pi, neck {neck/math.pi:.4f} pi, total {(sph+neck)/math.pi:.4f} pi (sphere area fraction not the full 4pi because a cap is cut)")
print("  with a small hole sphere -> 4pi, neck -> -4pi, total 0, independent of hole size")
