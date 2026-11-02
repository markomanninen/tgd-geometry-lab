# SO(3)-symmetric surfaces.  (1) Pitkanen's ansatz xi=tan(theta(r)/2) exp(i om t) on CP_1.
# (2) static geodesic profile with X=sin(psi): catenoid, cone, cubic first integral.
from pallo_uv_lib import *
I=mp.mpc(0,1); kap=mp.mpf(1)/2
def thdd(r,th,thp,om):
    W=1-kap**2*om**2*mp.sin(th)**2; WT=-2*kap**2*om**2*mp.sin(th)*mp.cos(th); S=mp.sqrt(1+kap**2*thp**2)
    return S**3/(r**2*mp.sqrt(W)*kap**2)*(r**2*S*WT/(2*mp.sqrt(W))-2*r*mp.sqrt(W)*kap**2*thp/S-r**2*WT*kap**2*thp**2/(2*mp.sqrt(W)*S))
def rk(th0,om,rmax,h):
    # start from the regular series theta=th0+c r^2
    r=mp.mpf('1e-3')
    W=1-kap**2*om**2*mp.sin(th0)**2; c=-om**2*mp.sin(th0)*mp.cos(th0)/(6*W)
    th=th0+c*r**2; p=2*c*r; out=[]
    while r<rmax:
        f=lambda r,y:(y[1],thdd(r,y[0],y[1],om))
        y=(th,p); k1=f(r,y); k2=f(r+h/2,(y[0]+h/2*k1[0],y[1]+h/2*k1[1])); k3=f(r+h/2,(y[0]+h/2*k2[0],y[1]+h/2*k2[1])); k4=f(r+h,(y[0]+h*k3[0],y[1]+h*k3[1]))
        th+=h/6*(k1[0]+2*k2[0]+2*k3[0]+k4[0]); p+=h/6*(k1[1]+2*k2[1]+2*k3[1]+k4[1]); r+=h
        out.append((r,th,p))
    return out
mp.mp.dps=20
om=mp.mpf(1); th0=mp.mpf('0.5')
tr=rk(th0,om,mp.mpf(40),mp.mpf('0.02'))
print('Pitkanen ansatz om=1 theta(0)=0.5; linear law sin(r)/r; envelope r*|theta|, and ratio to the linear solution')
for R in (2,5,10,20,30,40):
    q=min(tr,key=lambda e:abs(e[0]-R)); print(mp.nstr(q[0],5),'theta',mp.nstr(q[1],6),'r*sqrt(th^2+(th-prime)^2)',mp.nstr(q[0]*mp.sqrt(q[1]**2+q[2]**2),6),'linear',mp.nstr(th0*mp.sin(q[0])/q[0],6))
mp.mp.dps=40
def profile(r0,x,y,z,s):
    # s = [s0,s1,s2,s3]: Taylor coefficients in delta r
    r=(x*x+y*y+z*z).sqrt(); de=r-r0
    return s[0]+s[1]*de+s[2]*de*de*(mp.mpf(1)/2)+s[3]*de*de*de*(mp.mpf(1)/6)
PT=(mp.mpf('0.3'),mp.mpf('1.1'),mp.mpf('-0.7'),mp.mpf('0.5'))
t,x,y,z=[J.var(i,PT[i]) for i in range(4)]
r0=mp.sqrt(PT[1]**2+PT[2]**2+PT[3]**2)
# residual of the ODE on a generic point: put theta'' from the ODE, third derivative by finite difference is not needed for H
tv=mp.mpf('0.8'); pv=mp.mpf('-0.3'); ov=mp.mpf('1.2'); dd=thdd(r0,tv,pv,ov)
th=profile(r0,x,y,z,[tv,pv,dd,0])
xi=(th*(mp.mpf(1)/2)).sin()/(th*(mp.mpf(1)/2)).cos()*(t*I*ov).exp()
s=surface([t,x,y,z],[xi,J.const(0)])
print('ansatz, ODE at a point: H',mp.nstr(mx(s['H']),3),'(third derivative omitted, so E below is not used)')
th=profile(r0,x,y,z,[tv,pv,dd+mp.mpf('0.1'),0]); xi=(th*(mp.mpf(1)/2)).sin()/(th*(mp.mpf(1)/2)).cos()*(t*I*ov).exp()
print('same with theta-second-derivative off by 0.1: H',mp.nstr(mx(surface([t,x,y,z],[xi,J.const(0)])['H']),4))
def static(Xf,nm,L=None):
    Sf=lambda r: Xf(r)/mp.sqrt(1-Xf(r)**2)
    c=[mp.mpf('0.15'),Sf(r0),mp.diff(Sf,r0),mp.diff(Sf,r0,2)]
    sv=profile(r0,x,y,z,c); xi=sv.sin()/sv.cos()
    S=surface([t,x,y,z],[xi,J.const(0)])
    H=S['H'][4]; E=S['E'][4]
    sig1=mp.diff(lambda r:r**2*Xf(r),r0)/r0**2; sig3=mp.diff(lambda r:Xf(r)**3,r0)/(3*r0**2)
    print(f"{nm:26s} H {mp.nstr(abs(H),5)} E {mp.nstr(abs(E),5)} E/H {mp.nstr(mp.re(E/H) if abs(H)>1e-30 else 0,8)} 3sig3/sig1 {mp.nstr(3*sig3/sig1 if abs(sig1)>1e-30 else 0,8)}"+(f"  E-L H {mp.nstr(abs(E-L*H),3)}" if L is not None else ''))
C=mp.mpf('0.4')
static(lambda r:C/r**2,'catenoid X=C/r^2')
static(lambda r:mp.mpf('0.3'),'cone X=0.3')
L=mp.mpf('0.2')
def cub(r):
    return mp.re(mp.findroot(lambda X:X**3-L*r**2*X-C,mp.mpf('0.82')))
static(cub,'cubic X^3-L r^2 X=C',L)
a=mp.mpf(3); L2=1/a**2
static(lambda r:r/a,'round S^3 radius 3, X=r/a',L2)
