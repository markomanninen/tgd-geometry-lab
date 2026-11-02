# Cubic family x^3+y^3+z^3+(c/4) z (x+y)^2=0, Fermat at c=0, node at c=-3.
# Uniformisation by Weierstrass functions with g2=-4c, g3=8. Trapezoid rule on the torus.
import numpy as np
from scipy.optimize import brentq
sig=lambda k,n:sum(d**k for d in range(1,n+1) if n%d==0)
S3=np.array([sig(3,n) for n in range(1,40)],float);S5=np.array([sig(5,n) for n in range(1,40)],float)
def E46(y):
    q=-np.exp(-2*np.pi*y); p=q**np.arange(1,40)
    return 1+240*(S3*p).sum(),1-504*(S5*p).sum()
def lattice(c):
    if c==0: y=np.sqrt(3)/2
    else:
        f=lambda y:27*E46(y)[0]**3/E46(y)[1]**2-abs(c)**3
        y=brentq(f,np.sqrt(3)/2,12.0,xtol=1e-14)
    E4,E6=E46(y); om=np.pi*(E6/27)**(1/6)
    return 0.5+1j*y,om,y
def wp(c,Na,Nb):
    tau,om,y=lattice(c); g2=-4*c; g3=8.0
    a=(np.arange(Na)+.5)/Na; b=(np.arange(Nb)+.5)/Nb-.5
    A,B=np.meshgrid(a,b,indexing='ij'); w=np.exp(2j*np.pi*(A+B*tau))
    Q=np.exp(2j*np.pi*tau); pre=2j*np.pi/om
    M=int(min(14,6+30/(2*np.pi*y)))
    Qs=Q**np.arange(1,40); const=1/12-2*(Qs/(1-Qs)**2).sum()
    P=np.zeros_like(w); Pd=np.zeros_like(w)
    for n in range(-M,M+1):
        qw=Q**n*w; P+=qw/(1-qw)**2; Pd+=qw*(1+qw)/(1-qw)**3
    P=pre**2*(P+const); Pd=pre**3*Pd
    return tau,om,y,A,B,P,Pd,g2,g3
def geom(c,Na,Nb):
    tau,om,y,A,B,P,Pd,g2,g3=wp(c,Na,Nb)
    res=np.abs(Pd**2-(4*P**3-g2*P-g3))/(np.abs(Pd)**2+1)
    be=1/np.sqrt(24)
    Pdd=6*P**2-g2/2; Pddd=12*P*Pd
    p=np.stack([1+be*Pd,1-be*Pd,-P+0j]); p1=np.stack([be*Pdd,-be*Pdd,-Pd]); p2=np.stack([be*Pddd,-be*Pddd,-Pdd])
    n0=(np.abs(p)**2).sum(0)
    cr=np.cross(p,p1,axis=0); n1=(np.abs(cr)**2).sum(0)
    Lam2=(cr*p2).sum(0)   # det(p,p',p'')
    lam2=n1/n0**2
    K=4-2*n0**3*np.abs(Lam2)**2/n1**3
    du=abs(om)**2*tau.imag/(Na*Nb)
    # normal speed for d/dc
    u=p/np.sqrt(n0); x,yy,z=u
    Fc=z*(x+yy)**2/4; Fx=3*x**2+c/2*z*(x+yy); Fy=3*yy**2+c/2*z*(x+yy); Fz=3*z**2+c/4*(x+yy)**2
    xi2=np.abs(Fc)**2/(np.abs(Fx)**2+np.abs(Fy)**2+np.abs(Fz)**2)
    return dict(tau=tau,om=om,y=y,lam2=lam2,K=K,du=du,xi2=xi2,res=res.max(),B=B,Fres=np.abs(x**3+yy**3+z**3+c/4*z*(x+yy)**2).max())
print('Fermat and family: c, y, area/pi, intK, intK spectral, Kmin, Kmax, max cubic residual')
Rows=[]
for c,Na,Nb in [(0.0,256,256),(0.0,512,512),(-1.5,256,256),(-2.5,256,256),(-2.9,256,384),(-2.99,256,512),(-2.999,256,640),(-2.9999,256,768),(-2.99999,256,960),(-2.999999,256,1280)]:
    g=geom(c,Na,Nb); dA=g['lam2']*g['du']
    area=dA.sum(); iK=(g['K']*dA).sum()
    # spectral check of K from ln lam2 on the (a,b) grid: Delta_u in lattice coordinates
    t=g['tau'];om=g['om']; L=np.log(g['lam2']); Lh=np.fft.fft2(L)
    k=np.fft.fftfreq(Na,1/Na)[:,None]; l=np.fft.fftfreq(Nb,1/Nb)[None,:]
    lap=-(2*np.pi/om)**2*(abs(t)**2*k**2-2*t.real*k*l+l**2)/t.imag**2
    K2=-0.5*np.fft.ifft2(lap*Lh).real/g['lam2']
    iK2=(K2*dA).sum()
    neck=[(th,(g['K'][g['K']<th]*dA[g['K']<th]).sum()/np.pi,dA[g['K']<th].sum()/np.pi) for th in (0,-20)]
    Gv=(g['xi2']*dA).sum(); Gh=((4-2*g['K'])*g['xi2']*dA).sum()
    print(f"c={c:10.6f} Na={Na} Nb={Nb} y={g['y']:.4f} A/pi={area/np.pi:.10f} intK={iK:+.3e} spec={iK2:+.3e} Kmin={g['K'].min():.4e} Kmax={g['K'].max():.6f} res={g['res']:.1e},{g['Fres']:.1e} K<0:(intK/pi={neck[0][1]:.5f},A/pi={neck[0][2]:.5f}) K<-20:({neck[1][1]:.5f},{neck[1][2]:.6f}) G0={Gv:.5f} G1={Gh:.5e} (c+3)Kmin={(c+3)*g['K'].min():.4f} (c+3)G1={(c+3)*Gh:.4f}")
    Rows.append((c,Gv,Gh))
# proper distance along c with c_V->0 weight (units 8 pi G=1), weight G1 + Lambda G0
import numpy as np
cs=np.array([r[0] for r in Rows[2:]]+[]);
g=geom(0.0,256,256); K=g['K']; dA=g['lam2']*g['du']; A=dA.sum()
print('Fermat K range',K.min(),K.max())
for L in (1e-6,0.1,1,2,3,3.9,4,4.1):
    print(f'Lambda={L}: area share K>Lambda {dA[K>L].sum()/A:.4f}, share K>2+Lambda/2 {dA[K>2+L/2].sum()/A:.4f}, min w (8piG)={L-K.max():.4f}, min w_N={L+4-2*K.max():.4f}')
# spectrum of -Delta psi = mu^2 W psi, W=(1-K/Lambda) lam2, truncated Fourier basis
def spec(L,KK,N=256):
    g=geom(0.0,N,N); t=g['tau'];om=g['om']; W=(1-g['K']/L)*g['lam2']
    Wh=np.fft.fft2(W)/N**2
    ks=[(k,l) for k in range(-KK,KK+1) for l in range(-KK,KK+1) if (k,l)!=(0,0)]
    k=np.array([x[0] for x in ks]);l=np.array([x[1] for x in ks])
    D=(2*np.pi/om)**2*(abs(t)**2*k**2-2*t.real*k*l+l**2)/t.imag**2
    M=Wh[(k[:,None]-k[None,:])%N,(l[:,None]-l[None,:])%N]
    v=Wh[k%N,l%N]; M=M-np.outer(v,v.conj())/Wh[0,0]
    S=1/np.sqrt(D); Mx=(S[:,None]*M*S[None,:]); Mx=(Mx+Mx.conj().T)/2
    nu=np.linalg.eigvalsh(Mx)
    neg=nu[nu<-1e-10]; pos=nu[nu>1e-10]
    return len(neg),len(pos),(1/neg.min() if len(neg) else 0),(1/neg.max() if len(neg) else 0),(1/pos.max() if len(pos) else 0)
print('Lambda KK nneg npos slowest_tachyon mu2  fastest mu2  lowest positive mu2')
for L in (0.1,1.0,3.9,4.1,8.0):
    for KK in (6,10,14):
        print(L,KK,spec(L,KK))
