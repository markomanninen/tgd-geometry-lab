# Independent checks of P^{ab} sign/factor, Psi flux divergence, numbers, averaging of null curves.
import sympy as sp, numpy as np, mpmath as mp
r,Th,Psi,Phi,eps=sp.symbols('r Theta Psi Phi epsilon',positive=True)
X=[r,Th,Psi,Phi]; F=1+r**2   # R=1
a=r**2/(4*F**2); b=r**2/(4*F); c=sp.cos(Th); sn=sp.sin(Th)
s=sp.zeros(4); s[0,0]=1/F**2; s[1,1]=b; s[2,2]=a; s[2,3]=s[3,2]=a*c; s[3,3]=a*c**2+b*sn**2
# 1. first-order variation test: g=-s + eps*w(r) dr dr. Compare d/deps int sqrt|g| R with -int sqrt|g| G^{rr} w
w=r**5/F**6   # decays at both ends, boundary terms vanish
g=-s; g=g.as_mutable(); g[0,0]=g[0,0]+eps*w
gi=sp.zeros(4); g0=-s
gi0=g0.inv().applyfunc(sp.simplify)
dg=sp.zeros(4); dg[0,0]=w
gi1=(-gi0*dg*gi0).applyfunc(sp.simplify)
def T(e): # truncate to O(eps)
    return e
Gi=gi0+eps*gi1
n=4
def trunc(e):
    e=sp.series(sp.together(e),eps,0,2).removeO() if e.has(eps) else e
    return e
Gam=[[[ (sum(Gi[A,d]*(sp.diff(g[d,B],X[C])+sp.diff(g[d,C],X[B])-sp.diff(g[B,C],X[d])) for d in range(n))/2) for C in range(n)] for B in range(n)] for A in range(n)]
def E01(e):
    e=sp.expand(e); return e.coeff(eps,0)+eps*e.coeff(eps,1)
Gam=[[[E01(Gam[A][B][C]) for C in range(n)] for B in range(n)] for A in range(n)]
Ric=sp.zeros(n)
for B in range(n):
    for C in range(B,n):
        e=0
        for A in range(n):
            e+=sp.diff(Gam[A][B][C],X[A])-sp.diff(Gam[A][B][A],X[C])
            for d in range(n):
                e+=Gam[A][A][d]*Gam[d][B][C]-Gam[A][C][d]*Gam[d][B][A]
        Ric[B,C]=Ric[C,B]=E01(e)
Rs=E01(sum(Gi[i,j]*Ric[i,j] for i in range(n) for j in range(n)))
R0=sp.simplify(Rs.coeff(eps,0)); R1=Rs.coeff(eps,1)
sq0=r**3*sn/(8*F**3)
sq1=sq0*sp.Rational(1,2)*gi0[0,0]*w          # d sqrt|g| / d eps
print('R0 =',R0)
dens_R=sq1*R0+sq0*R1                          # d(sqrt g R)/d eps
Gup_rr=6*gi0[0,0]                             # G^{ab}=k g^{ab}, k=6
pred=-sq0*Gup_rr*w                            # -sqrt g G^{rr} w
fR=sp.lambdify((r,Th),dens_R,'mpmath'); fP=sp.lambdify((r,Th),pred,'mpmath')
th0=mp.mpf(1)  # Theta factor is sin(Th) in both after averaging; compare radial integrals at fixed Theta
I1=mp.quad(lambda x:fR(x,th0),[0,1,5,mp.inf]); I2=mp.quad(lambda x:fP(x,th0),[0,1,5,mp.inf])
print('d/deps int sqrt g R (fixed Theta)=',I1,'  predicted -int sqrt g G^rr w =',I2)
# scale check
print('scaling: dS/deps for g->(1+2eps)g gives Vol*(4cV+2cR*R), formula E^ab*2g_ab gives same with g_ab G^ab=4k=-R')
# 2. Psi flux: integrand sqrt s * s^{PsiPsi} ~ 1/sin(Theta)
si=s.inv().applyfunc(sp.simplify); sqs=r**3*sn/(8*F**3)
e=sp.simplify(sqs*si[2,2]); print('sqrt s s^{PsiPsi} =',e,'  (1/sin Theta at Theta->0: log divergent flux)')
# 3. numbers
MP=1.22089e19; me=0.51099895e-3; hbarc_fm=0.1973269804
R_lp=np.sqrt(1e7); RoverG=R_lp*MP; mCP=MP/R_lp
print('sqrt(R^2/G)=',R_lp,' 1/R GeV=',mCP,' R/G GeV=',RoverG)
Cav=0.75*RoverG; Cmax=6/(8*np.pi)*6.41049610*RoverG; Char=1.5*np.pi*RoverG
for nm,C in [('keskiarvo 3/4',Cav),('huippu',Cmax),('harmoninen 3pi/2',Char)]:
    print(nm,'C/(R/G)=',C/RoverG,' C GeV=',C,' dt/ds(me)=',me/C,' 1-v^2 for tdot=1:',(me/C)**2)
pM127=2**127-1
print('m_e R=',me/mCP,' 1/sqrt(p)=',pM127**-0.5,' (G/R^2)/sqrt p=',1e-7*pM127**-0.5)
print('L = 2 G m_e/(3 pi) in GeV^-1=',2*me/(3*np.pi*MP**2),' in m=',2*me/(3*np.pi*MP**2)*hbarc_fm*1e-15)
print('R in m (lP=1.616e-35)=',R_lp*1.616e-35,' Compton_e m=',2*np.pi*hbarc_fm*1e-15/me)
print('S_R(CP2)=-(3pi/4)R^2/G=',-3*np.pi/4*1e7)
# 4. random null curve average: tdot=1, random unit directions, piecewise constant
rng=np.random.default_rng(1)
for N in [10,1000,100000]:
    v=rng.normal(size=(N,3)); v/=np.linalg.norm(v,axis=1,keepdims=True)
    vb=v.mean(axis=0); print('N',N,'|vbar|=',np.linalg.norm(vb),' M/(C<tdot>)=',np.sqrt(1-vb@vb))
