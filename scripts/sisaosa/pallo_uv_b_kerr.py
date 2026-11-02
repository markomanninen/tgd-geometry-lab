# Direction function Y of a shear-free congruence.  a = A + Y B, b = C + Y D are linear in x.
# G(Y,a,b) = 0 fixes Y(x).  The cone from the time axis is b = a Y, with Y = w and a = -u.
from pallo_uv_lib import *
I=mp.mpc(0,1)
PTS=[(0.3,1.1,-0.7,0.5),(-0.4,0.6,1.3,-0.9),(1.2,-1.5,0.4,0.8)]
def coords(p):
    t,x,y,z=[J.var(i,p[i]) for i in range(4)]
    A=z-t; B=x-y*I; C=x+y*I; D=-(t+z)
    return t,x,y,z,A,B,C,D
def wcoord(x,y,z):
    r=(x*x+y*y+z*z).sqrt(); return (x+y*I)/(r+z), r
def solveY(p,g,gY,ga,eps):
    t,x,y,z,A,B,C,D=coords(p)
    w,r=wcoord(x,y,z)
    def G(Y):
        a=A+Y*B; b=C+Y*D
        return b-a*Y-eps*g(Y,a), D-a-Y*B-eps*(gY(Y,a)+ga(Y,a)*B), a, b
    # constant term by Newton on numbers, then on jets
    Y=J.const(w.v())
    for _ in range(40):
        f,df,_,_=G(Y); Y=J.const(Y.v()-f.v()/df.v())
    Y=Y+ (w-w)  # keeps the type
    for _ in range(6):
        f,df,_,_=G(Y); Y=Y-f/df
    f,df,a,b=G(Y)
    return Y,a,b,df,(t,x,y,z),w,r,mx(f.c)
CASES={
 'g=0 (kartio)':(lambda Y,a:J.const(0),lambda Y,a:J.const(0),lambda Y,a:J.const(0)),
 'g=Y^3':(lambda Y,a:Y*Y*Y,lambda Y,a:3*Y*Y,lambda Y,a:J.const(0)),
 'g=a^2 Y':(lambda Y,a:a*a*Y,lambda Y,a:a*a,lambda Y,a:2*a*Y),
 'g=exp(i a)':(lambda Y,a:(a*I).exp(),lambda Y,a:J.const(0),lambda Y,a:(a*I).exp()*I),
 'g=sin(a) Y^3':(lambda Y,a:a.sin()*Y*Y*Y,lambda Y,a:a.sin()*3*Y*Y,lambda Y,a:a.cos()*Y*Y*Y),
}
if __name__=='__main__':
    EPS=mp.mpf('0.1')
    print('Y from G=b-aY-eps g(Y,a)=0, eps=0.1. Columns: residual of G, |(grad Y)^2|, |box Y|, |box a-4 G_b/G_Y|, H, G^abB_ab for xi=Y, then for xi=(Y,Y^2), r*(Y-w)')
    for nm,(g,gY,ga) in CASES.items():
        for p in PTS:
            Y,a,b,df,X,w,r,res=solveY(p,g,gY,ga,EPS)
            nul=dot(Y,Y).v(); bx=box(Y)
            pa=box(a)-4/df.v()
            S=surface(list(X),[Y,J.const(0)])
            S2=surface(list(X),[Y,Y*Y])
            print(f"{nm:14s} res {mp.nstr(res,3):9s} null {mp.nstr(abs(nul),3):9s} box {mp.nstr(abs(bx),3):9s} boxa {mp.nstr(abs(pa),3):9s} H {mp.nstr(mx(S['H']),3):9s} E {mp.nstr(mx(S['E']),5):11s} H2 {mp.nstr(mx(S2['H']),3):9s} E2 {mp.nstr(mx(S2['E']),5):11s} r*dY {mp.nstr(r.v()*(Y.v()-w.v()),6)}")
    # leading-order formula Y = w - eps g(w,-u)/(2 r), at growing radius
    print('large r, g=exp(i a): r(Y-w) against -eps g(w,-u)/2')
    g,gY,ga=CASES['g=exp(i a)']
    for s in (10,100,1000):
        p=(0.3,1.1*s,-0.7*s,0.5*s)
        Y,a,b,df,X,w,r,res=solveY(p,g,gY,ga,EPS)
        u=X[0].v()-r.v()
        print(s,mp.nstr(r.v()*(Y.v()-w.v()),10),mp.nstr(-EPS*mp.exp(-I*u)/2,10),'dY/dwbar coefficient grows? |Y-w|',mp.nstr(abs(Y.v()-w.v()),4))
    # rotation test: the surface is not SO(3) symmetric and depends on t
    print('dependence on t and on direction: Y(t) at fixed x, g=exp(i a)')
    for t0 in (0,0.5,1.0):
        p=(t0,1.1,-0.7,0.5); Y,a,b,df,X,w,r,res=solveY(p,g,gY,ga,EPS); print(t0,mp.nstr(Y.v(),8),'w',mp.nstr(w.v(),8))
    # real moving vertex: z(tau)=(tau,eps sin tau,0,0), retarded time and direction
    print('real moving vertex z(tau)=(tau, e sin tau, 0, 0), e=0.3: direct retarded Y')
    e=mp.mpf('0.3')
    for p in PTS:
        t,x,y,z,A,B,C,D=coords(p)
        tau=J.const(0)
        tv=p[0]-1
        F=lambda tt:(p[0]-tt)-mp.sqrt((p[1]-e*mp.sin(tt))**2+p[2]**2+p[3]**2)
        tv=mp.re(mp.findroot(F,tv))
        tau=J.const(tv)+(t-t)
        for _ in range(6):
            dx=x-e*tau.sin(); R2=dx*dx+y*y+z*z; f=(t-tau)*(t-tau)-R2
            df=(tau-t)*2+dx*2*e*tau.cos()
            tau=tau-f/df
        dx=x-e*tau.sin(); R=(t-tau)
        Y=(dx+y*I)/(R+z)
        S=surface([t,x,y,z],[Y,J.const(0)]); S2=surface([t,x,y,z],[Y,Y*Y])
        print('null',mp.nstr(abs(dot(Y,Y).v()),3),'box',mp.nstr(abs(box(Y)),3),'H',mp.nstr(mx(S['H']),3),'E line',mp.nstr(mx(S['E']),5),'E conic',mp.nstr(mx(S2['E']),5))

