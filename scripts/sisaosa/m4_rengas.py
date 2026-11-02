# Flux surfaces of a current ring against parallel tori; two coaxial rings; periods of y^2=F(w).
import numpy as np
from scipy.special import ellipk,ellipe
from scipy.integrate import quad
def S(rho,z,R=1.0):
    m=4*R*rho/((R+rho)**2+z**2); k=np.sqrt(m)
    return rho*np.sqrt(R/rho)/k*((2-m)*ellipk(m)-2*ellipe(m))
def gradS(rho,z,h=1e-5):
    return (S(rho+h,z)-S(rho-h,z))/(2*h),(S(rho,z+h)-S(rho,z-h))/(2*h)
from scipy.optimize import brentq
print("ring flux surface: level through (1+f,0). columns: f, inner f at z=0, centre shift, |gradS| max/min, eikonal defect")
for f in [0.02,0.1,0.3,0.5,0.8]:
    S0=S(1+f,0.0)
    th=np.linspace(0,np.pi,181); pts=[]
    # centre on ring point, polar search
    for a in th:
        g=lambda r:S(1+r*np.cos(a),r*np.sin(a))-S0
        lo=1e-4; hi=f*3
        if 1+hi*np.cos(a)<=0: hi=(1-1e-3)/(-np.cos(a))
        try: r=brentq(g,lo,hi)
        except: r=np.nan
        pts.append(r)
    pts=np.array(pts); inner=pts[-1]
    # |grad S|/rho is the field strength; level-parallel test uses |grad S| itself
    G=[np.hypot(*gradS(1+r*np.cos(a),r*np.sin(a))) for a,r in zip(th,pts) if r==r]
    print(f"f={f:.2f} inner={inner:.4f} shift={(f-inner)/2:.4f} |gradS| max/min={max(G)/min(G):.3f}")
print("axis passage: S=0 only on axis, ring is a maximum of S; every level S>0 near ring is one closed curve in half plane -> torus")
print("level curves far from ring: also closed curves around the ring reaching toward axis, S->0 at axis and at infinity")
print("--- two coaxial rings same current, R=1, z=+-0.6: critical points of S on half plane")
def S2(r,z,s=1): return S(r,z-0.6)+s*S(r,z+0.6)
for s in (1,-1):
    rs=np.linspace(0.2,2,181); zs=np.linspace(-1.5,1.5,301)
    P=np.array([[S2(r,zz,s) if not(abs(r-1)<1e-9 and abs(abs(zz)-.6)<1e-9) else np.nan for zz in zs] for r in rs])
    Gr,Gz=np.gradient(P,rs,zs); Hrr=np.gradient(Gr,rs,axis=0);Hzz=np.gradient(Gz,zs,axis=1);Hrz=np.gradient(Gr,zs,axis=1)
    Nn=np.hypot(Gr,Gz); crit=[]
    for i in range(2,179):
        for j in range(2,299):
            if Nn[i,j]==np.nanmin(Nn[i-2:i+3,j-2:j+3]) and Nn[i,j]<0.08 :
                crit.append((round(rs[i],2),round(zs[j],2),"saddle" if Hrr[i,j]*Hzz[i,j]-Hrz[i,j]**2<0 else "extremum"))
    print("s=",s,crit)
print("--- double cover y^2=F(w), n=2, axes at angle alpha: a1=0,b1=inf,a2=tan(alpha/2),b2=-1/a2")
for al in [90,60,30,10]:
    a=np.tan(np.radians(al)/2)
    p=lambda w:w*(w-a)*(1+a*w)
    w1=quad(lambda s:2*s/np.sqrt(abs(p(s**2))),0,np.sqrt(a),limit=400)[0]        # 0..a
    w2=quad(lambda s:2*s/np.sqrt(abs(p(-s**2))),0,1/np.sqrt(a),limit=400)[0]      # -1/a..0
    print(f"alpha={al}  period ratio (imag tau) = {w1/w2:.5f}  inverse {w2/w1:.5f}")
