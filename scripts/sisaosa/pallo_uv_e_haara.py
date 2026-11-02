# y^2 = F(w) on (u,v) x Sigma, in the chart s=y, so that the branch point is an ordinary point.
# X^4: (u,v,s) -> (t, r n(w(s)), xi=s).  Also the chart w away from branch points.
from pallo_uv_lib import *
import numpy as np
I=mp.mpc(0,1)
AS=[mp.mpc('0.3','0.2'),mp.mpc('-0.5','0.7')]
def Fn(w,AS):
    r=J.const(1)
    for a in AS: r=r*(w-a)/(1+mp.conj(a)*w)
    return r
def dFn(w,AS):
    # product rule, safe at a zero of F
    tot=J.const(0)
    for i,a in enumerate(AS):
        t=J.const(1)
        for j,b in enumerate(AS):
            t=t*(1+mp.conj(b)*w).inv()
            if j!=i: t=t*(w-b)
        t=t*(1-(w-a)*mp.conj(a)*(1+mp.conj(a)*w).inv())
        tot=tot+t
    return tot
def wofy(y,w0,AS):
    w=J.const(w0)
    y2=y*y
    for _ in range(60):
        f=Fn(w,AS)-y.v()**2; fd=dFn(w,AS); w=J.const(w.v()-f.c[0]/fd.c[0])
    for _ in range(6):
        w=w-(Fn(w,AS)-y2)/dFn(w,AS)
    return w
def evalpt(U,V,y0,w0,AS,target=lambda y:y,verbose=True):
    u=J.var(0,U); v=J.var(1,V); p=J.var(2,mp.re(y0)); q=J.var(3,mp.im(y0))
    y=p+q*I; yb=p-q*I
    w=wofy(y,w0,AS); wb=w.conj()
    X=sph_chart(u,v,w,wb)
    S=surface(X,[y,J.const(0)])
    r=(V-U)/2
    rho=4/((1+w*wb)*(1+w*wb))
    ws=(w.d(2)-w.d(3)*I)*(mp.mpf(1)/2)
    Pj=rho*ws*ws.conj()
    Qj=(1+y*yb).inv()*(1+y*yb).inv()
    Phi=Pj*(r*r)+Qj
    # R formula: 4P/Phi-2r^2P^2/Phi^2+(1/Phi) Laplacian log Phi  (r is a jet in u,v only through Phi here)
    rj=(v-u)*(mp.mpf(1)/2)
    Ph=Pj*(rj*rj)+Qj
    Lg=Ph.d(2)*(Ph.inv())
    Lh=Ph.d(3)*(Ph.inv())
    lap=(Lg.d(2)+Lh.d(3)).v()
    Rf=(4*Pj.v()/Ph.v()-2*r**2*Pj.v()**2/Ph.v()**2+lap/Ph.v())
    # q = Q P_sbar - Q_sbar P
    Ps=(Pj.d(2)+Pj.d(3)*I)*(mp.mpf(1)/2); Qs=(Qj.d(2)+Qj.d(3)*I)*(mp.mpf(1)/2)
    qq=(Qj*Ps-Qs*Pj).v()
    Ef=4*Pj.v()*qq*r**2/Ph.v()**4
    return dict(S=S,w=w.v(),Phi=Ph.v(),Rf=Rf,Ef=Ef,detg=mp.det(S['g']),g33=S['g'][2,2])
U,V=mp.mpf('0.3'),mp.mpf('2.5')
print('n=2 a1,a2=',AS,'genus 1, r=',(V-U)/2)
print('columns: y, |H|max, E^xi(num), E^xi(formula), |E_M4|max, R(num), R(formula), Phi, det g')
for y0,w0 in [(mp.mpc(0),AS[0]),(mp.mpc('0.05','0.02'),AS[0]),(mp.mpc('0.2','0.1'),AS[0]),(mp.mpc('0.6','-0.3'),AS[0]+mp.mpc('0.1','0.1')),(mp.mpc(0),AS[1])]:
    d=evalpt(U,V,y0,w0,AS); S=d['S']
    print(mp.nstr(y0,4),'H',mp.nstr(mx(S['H']),3),'Exi',mp.nstr(S['E'][4],6),'f',mp.nstr(d['Ef'],6),'EM',mp.nstr(mx(S['E'][:4]),5),'R',mp.nstr(mp.re(S['R']),8),mp.nstr(mp.re(d['Rf']),8),'Phi',mp.nstr(mp.re(d['Phi']),6),'det',mp.nstr(mp.re(d['detg']),6),'w',mp.nstr(d['w'],5))
print('near the zero, E_M4/|y|^2 and E_xi/|y|^3 as y->0 along one ray')
for t_ in ('0.1','0.03','0.01','0.003'):
    y0=mp.mpf(t_)*mp.mpc('0.8','0.6')
    d=evalpt(U,V,y0,AS[0],AS); S=d['S']
    print(t_,mp.nstr(mx(S['E'][:4])/abs(y0)**2,6),mp.nstr(abs(S['E'][4])/abs(y0)**3,6))
print('bad case: double zero a1=a2 gives no chart y; F~(w-a)^2 means y=+-c(w-a): two sheets cross (node).')
# global integrals on Sigma, chart w on the sphere, two sheets
def integrals(As,r,N=1600):
    th=(np.arange(N)+.5)*np.pi/N; ph=(np.arange(2*N)+.5)*np.pi/N
    TH,PH=np.meshgrid(th,ph,indexing='ij')
    w=np.tan(TH/2)*np.exp(1j*PH)
    dA=np.sin(TH)*(np.pi/N)**2   # area on the unit sphere = rho d^2w
    F=np.ones_like(w); L=np.zeros_like(w)
    for a in As:
        a=complex(a); F=F*(w-a)/(1+np.conj(a)*w); L=L+1/(w-a)-np.conj(a)/(1+np.conj(a)*w)
    Fp=F*L
    om=np.abs(Fp)**2/(4*np.abs(F)*(1+np.abs(F))**2)      # h |y_w|^2
    rho=4/(1+np.abs(w)**2)**2
    ratio=om/rho                                          # Q/P
    area=2*np.sum(ratio*dA)
    I_=2*np.sum(ratio/(r**2+ratio)*dA)
    return area/np.pi, I_
print('n, area_CP1/pi from the integral, I(r) for several r')
for As in ([0j],[0.3+0.2j,-0.5+0.7j],[0.3+0.2j,-0.3+0.2j],[1j*0.1,0.1],[0.3+0.2j,-0.5+0.7j,1.2-0.4j]):
    print(As,[tuple(round(x,4) for x in integrals(As,r)) for r in (0.0001,0.5,1.0,3.0)])
