# Exact a=3 extremal, a=1 Bjorling form, checks of the boundary analysis.
import sympy as sp, numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
t,s=sp.symbols('t s',real=True)
def geom(F):
    Ft=[sp.diff(f,t) for f in F]; Fs=[sp.diff(f,s) for f in F]
    Am=sp.Matrix([[0,sp.Rational(1,2),0],[sp.Rational(1,2),0,0],[0,0,-1]])  # dU dV - dW^2
    a=sp.Matrix(Ft); b=sp.Matrix(Fs)
    E=sp.expand((a.T*Am*a)[0]); G2=sp.expand((a.T*Am*b)[0]); Gs=sp.expand((b.T*Am*b)[0])
    return a,b,E,G2,Gs
U=t*s**3+t**3*s**4/9+t**5*s**5/405; V=t; W=3*s+s**2*t**2/6
a,b,E,M,Gg=geom([U,V,W])
Om=1+s*t**2/9
print('g_vv-s^3 Om^2 =',sp.simplify(E-s**3*Om**2),' g_vs-(t s^2/2)Om^2 =',sp.simplify(M-t*s**2/2*Om**2),' g_ss+9 Om^2 =',sp.simplify(Gg+9*Om**2))
D=sp.factor(E*Gg-M**2); print('det g_2 =',D)
# mean curvature: covariant normal nu_a = eps_abc a^b b^c
nu=a.cross(b)
Fvv=sp.Matrix([sp.diff(f,t,2) for f in (U,V,W)]);Fvs=sp.Matrix([sp.diff(sp.diff(f,t),s) for f in (U,V,W)]);Fss=sp.Matrix([sp.diff(f,s,2) for f in (U,V,W)])
H=Gg*(nu.dot(Fvv))-2*M*(nu.dot(Fvs))+E*(nu.dot(Fss))
print('mean curvature numerator =',sp.expand(H))
# second check by null curves: A(k)=(3/5k^5,-3/k,3/2k^2), F=A(-k1)+A(k2)
k1,k2=sp.symbols('k1 k2',positive=True)
A=lambda k:sp.Matrix([sp.Rational(3,5)*k**5,-3/k,sp.Rational(3,2)*k**2])
Fn=A(-k1)+A(k2); sig=k1*k2; v=3*(k2-k1)/sig
print('param match:',[sp.simplify(Fn[i]-e.subs({t:v,s:sig})) for i,e in enumerate((U,V,W))])
print('null check A1:',sp.simplify(sp.diff(A(k1),k1)[0]*sp.diff(A(k1),k1)[1]-sp.diff(A(k1),k1)[2]**2))
# 2D curvature
def R2(g,xs):
    gi=g.inv(); n=2
    Gam=[[[sum(gi[i,l]*(sp.diff(g[l,j],xs[k])+sp.diff(g[l,k],xs[j])-sp.diff(g[j,k],xs[l])) for l in range(n))/2 for k in range(n)] for j in range(n)] for i in range(n)]
    Ric=sp.zeros(n)
    for j in range(n):
        for k in range(n):
            Ric[j,k]=sum(sp.diff(Gam[i][j][k],xs[i]) for i in range(n))-sum(sp.diff(Gam[i][j][i],xs[k]) for i in range(n))+sum(Gam[i][i][l]*Gam[l][j][k]-Gam[i][k][l]*Gam[l][j][i] for i in range(n) for l in range(n))
    return sp.simplify(sum(gi[i,j]*Ric[i,j] for i in range(n) for j in range(n)))
g=sp.Matrix([[E,M],[M,Gg]]); Rr=sp.factor(R2(g,[t,s])); print('R =',Rr)
print('s^2 R at s->0:',sp.limit(s**2*Rr,s,0),' on t=0')
# GHY-type cut term on s=eps: N^2=-det/g_ss, B ~ d_n sqrt|h|
# order 5 from A(k)=5(k^7/7,-1/(3k^3),k^2/2): series check of g_vv order
d,sg=sp.symbols('d sg')
kp=(d+sp.sqrt(d**2+4*sg))/2; km=(-d+sp.sqrt(d**2+4*sg))/2 # k2=kp,k1=km, k1 k2=sg, k2-k1=d
# numerical check of order 5: g_vv/s^5 -> const at fixed v
def F5(k1,k2):
    return np.array([5*(k2**7-k1**7)/7, 5/3*(1/k1**3-1/k2**3), 2.5*(k1**2+k2**2)])
def chart(v,sigma):
    f=lambda de:5/3*(((-de+np.sqrt(de*de+4*sigma))/2)**-3-((de+np.sqrt(de*de+4*sigma))/2)**-3)-v
    de=brentq(f,0,1.0)
    return (-de+np.sqrt(de*de+4*sigma))/2,(de+np.sqrt(de*de+4*sigma))/2
for sg_ in [0.08,0.04,0.02]:
    h=1e-4; v0=1.0
    k1p,k2p=chart(v0+h,sg_); k1m,k2m=chart(v0-h,sg_)
    dF=(F5(k1p,k2p)-F5(k1m,k2m))/(2*h)
    gvv=dF[0]*dF[1]-dF[2]**2
    print('k=5 sigma',sg_,' g_vv/sigma^5 =',gvv/sg_**5)
# unfolding example: exact ZMC with a1 != 0 removes the triple zero
c,e=sp.symbols('c e')
# toy non-differentiability of the first-order action
for aa in (1,2,3,5):
    def Fa(sv):
        fn=lambda n:np.sqrt(abs(np.sign(n)**(aa)*abs(n)**aa+sv))
        pts=[0.0]+([-sv**(1/aa)] if aa%2 else [])
        return quad(fn,-1,1,points=pts,limit=400)[0]
    F0=Fa(0.0); vals=[(sv,Fa(sv)-F0) for sv in (1e-3,1e-4,1e-5,1e-6)]
    sl=[np.log(vals[i][1]/vals[i+1][1])/np.log(10) if vals[i][1]*vals[i+1][1]>0 else float('nan') for i in range(3)]
    print('a',aa,' dS(s) ',[f'{x[1]:.3e}' for x in vals],' exponent ',[f'{x:.3f}' for x in sl],' theory ',0.5+1/aa)
# rata-virta model: mean curvature of the section at D=0
aA,nA,r0=1.0,0.8,1.1
rho=np.sqrt(aA**2*r0**2/(nA**2+r0**2)); print('rho_Sigma',rho)
eta0,th0=0.7,0.4
X=lambda p:np.array([p[0]*np.sinh(p[2]),p[0]*np.cosh(p[2]),p[1]*np.cos(p[3]),p[1]*np.sin(p[3]),aA*p[2]+nA*p[3]])
eta5=np.diag([1.,-1,-1,-1,-1])
hd=1e-4; p0=np.array([rho,r0,eta0,th0])
Dv=[(X(p0+hd*np.eye(4)[i])-X(p0-hd*np.eye(4)[i]))/(2*hd) for i in range(4)]
DD=[[ (X(p0+hd*np.eye(4)[i]+hd*np.eye(4)[j])-X(p0+hd*np.eye(4)[i]-hd*np.eye(4)[j])-X(p0-hd*np.eye(4)[i]+hd*np.eye(4)[j])+X(p0-hd*np.eye(4)[i]-hd*np.eye(4)[j]))/(4*hd*hd) for j in range(4)] for i in range(4)]
T=np.array(Dv)
# normal covector in 5D
Mt=T@eta5
from numpy.linalg import svd
u_,s_,vt=svd(Mt); nuv=vt[-1]
Bm=np.array([[DD[i][j]@eta5@nuv for j in range(4)] for i in range(4)])
g4=T@eta5@T.T
print('det g4',np.linalg.det(g4))
gr=D2=None
# kernel in (eta,theta)
gb=g4[2:,2:]; w,vv=np.linalg.eigh(gb); e2=vv[:,np.argmin(abs(w))]; print('kernel eig',w)
# K_ij: 1/2 d_n q_ij for eta,theta block; n along grad D
Df=lambda rh,r:rh**2*(nA**2+r**2)-aA**2*r**2
grad=np.array([2*rho*(nA**2+r0**2),2*r0*(rho**2-aA**2)])
gper=np.array([grad[1],-grad[0]])/np.linalg.norm(grad)
nvec=grad/np.linalg.norm(grad)/np.sqrt(abs((grad/np.linalg.norm(grad))@g4[:2,:2]@(grad/np.linalg.norm(grad))))
dq=np.array([[2*rho*nvec[0],0.0],[0.0,-2*r0*nvec[1]]])/2 # K block on (eta,theta)
Ee=np.array([-e2[1],e2[0]]); 
c=-(Ee@dq@e2)/(e2@dq@e2); E2=Ee+c*e2
print('K(e,e)',e2@dq@e2,' K(e,E2)',E2@dq@e2)
E1v=np.r_[gper,0,0]; E2v=np.r_[0,0,E2]; ev=np.r_[0,0,e2]
Htil=(E1v@Bm@E1v)/(E1v@g4@E1v)+(E2v@Bm@E2v)/(E2v@g4@E2v)
print('H_tilde canonical =',Htil,'  B(e,e)',ev@Bm@ev,' B(E1,E2)',E1v@Bm@E2v,' B(E1,e)',E1v@Bm@ev)
print('terms',(E1v@Bm@E1v)/(E1v@g4@E1v),(E2v@Bm@E2v)/(E2v@g4@E2v))
