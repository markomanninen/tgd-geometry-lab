# Weighted forms in the spherical chart (u,v,a,b), w=a+ib.
from pallo_uv_lib import *
from pallo_uv_b_kerr import solveY, CASES
I=mp.mpc(0,1)
P0=[(mp.mpf('0.3'),mp.mpf('2.5'),mp.mpf('0.4'),mp.mpf('-0.6')),(mp.mpf('-0.5'),mp.mpf('3'),mp.mpf('0.25'),mp.mpf('0.125'))]
def ch(p):
    u,v,a,b=[J.var(i,p[i]) for i in range(4)]
    w=a+b*I; wb=a-b*I; r=(v-u)*(mp.mpf(1)/2)
    return u,v,w,wb,r,sph_chart(u,v,w,wb)
def mdot(f,h,u_i=(0,1)):
    # flat metric in the chart: m(df,dh) = 2(f_u h_v+f_v h_u) - (1/(r^2 rho))(f_a h_a+f_b h_b)
    return None
FAM={'w/r':lambda u,v,w,r:w/r,'u w/r':lambda u,v,w,r:u*w/r,'exp(iu) w^2/r':lambda u,v,w,r:(u*I).exp()*w*w/r,
     '(w+v w^2)/r':lambda u,v,w,r:(w+v*w*w)/r,'exp(iu)/r':lambda u,v,w,r:(u*I).exp()/r}
print('--- xi = eps F/r: H/eps^3 against S=(1/2)m(dxib,dP)-2 xib P, P=m(dxi,dxi). also d_wbar S')
for nm,f in FAM.items():
    for p in P0[:1]:
        u,v,w,wb,r,X=ch(p)
        x1=f(u,v,w,r); x1b=x1.conj()
        rho=4/((1+w*wb)*(1+w*wb))
        # flat Laplacian in the chart
        def m(f1,f2):
            return (f1.d(0)*f2.d(1)+f1.d(1)*f2.d(0))*2-(f1.d(2)*f2.d(2)+f1.d(3)*f2.d(3))/(r*r*rho)
        P=m(x1,x1); S=m(x1b,P)*(mp.mpf(1)/2)-2*x1b*P
        dSwb=(S.d(2)+S.d(3)*I)*(mp.mpf(1)/2)
        boxflat=(x1.d(0).d(1)*4-(x1.d(1)*2-x1.d(0)*2)/r-(x1.d(2).d(2)+x1.d(3).d(3))/(r*r*rho)).v()
        rs=[]
        for e in (mp.mpf('1e-3'),mp.mpf('1e-5')):
            s=surface(X,[x1*e,J.const(0)]); rs.append(s['H'][4]/e**3)
        s=surface(X,[x1*mp.mpf('0.2'),J.const(0)])
        print(f"{nm:16s} box {mp.nstr(abs(boxflat),3)} H/e^3 {mp.nstr(rs[1],8)} S {mp.nstr(S.v(),8)} |d_wbS| {mp.nstr(abs(dSwb.v()),5)} H(eps=.2) {mp.nstr(abs(s['H'][4]),5)} E/H {mp.nstr(abs(s['E'][4]/s['H'][4]),4)}")
print('--- around xi=w: which weight solves H=0 at first order? |H|/eps for xi=w+eps r^-p F(u,w)')
for nm,F in {'exp(iu)':lambda u,w:(u*I).exp(),'u w^3':lambda u,w:u*w*w*w,'exp(iu) w^2+1/(w-2)':lambda u,w:(u*I).exp()*w*w+(w-2).inv()}.items():
    for pw in (0,1,2):
        out=[]
        for e in (mp.mpf('1e-6'),mp.mpf('1e-8')):
            u,v,w,wb,r,X=ch(P0[0])
            wei=J.const(1)
            for _ in range(pw): wei=wei/r
            s=surface(X,[w+wei*F(u,w)*e,J.const(0)]); out.append(abs(s['H'][4])/e)
        print(f"{nm:22s} p={pw} {mp.nstr(out[0],6)} {mp.nstr(out[1],6)}")
print('--- exact Y in the spherical chart: dY/dwbar, solved directly')
def Ysph(p,g,gY,ga,eps):
    u,v,w,wb,r,X=ch(p); t,x,y,z=X
    A=z-t; B=x-y*I; C=x+y*I; D=-(t+z)
    def G(Y):
        a=A+Y*B; b=C+Y*D
        return b-a*Y-eps*g(Y,a), D-a-Y*B-eps*(gY(Y,a)+ga(Y,a)*B)
    Y=J.const(w.v())
    for _ in range(40):
        f,df=G(Y); Y=J.const(Y.v()-f.v()/df.v())
    for _ in range(6):
        f,df=G(Y); Y=Y-f/df
    return Y
for nm in ('g=Y^3','g=exp(i a)'):
    g,gY,ga=CASES[nm]
    for e in (mp.mpf('0.1'),mp.mpf('0.01')):
        Y=Ysph(P0[0],g,gY,ga,e)
        print(nm,'eps',e,'|dY/dwbar|',mp.nstr(abs((Y.d(2)+Y.d(3)*I).v()/2),5),'|dY/dv|',mp.nstr(abs(Y.d(1).v()),5),'|dY/du|',mp.nstr(abs(Y.d(0).v()),5))
print('--- translations and complex shift (Kerr congruence)')
PT=(0.3,1.1,-0.7,0.5)
t,x,y,z=[J.var(i,PT[i]) for i in range(4)]
for nm,d in {'real shift':(mp.mpf('0.2'),mp.mpf('-0.1'),mp.mpf('0.3')),'complex shift z-ia':(0,0,mp.mpc(0,0.4)),'complex shift, general':(mp.mpc(0.1,0.2),mp.mpc(0,-0.1),mp.mpc(0.2,0.3))}.items():
    X_,Y_,Z_=x-d[0],y-d[1],z-d[2]
    R=(X_*X_+Y_*Y_+Z_*Z_).sqrt(); Y=(X_+Y_*I)/(R+Z_)
    s=surface([t,x,y,z],[Y,J.const(0)])
    print(f"{nm:24s} null {mp.nstr(abs(dot(Y,Y).v()),3)} box {mp.nstr(abs(box(Y)),3)} H {mp.nstr(mx(s['H']),3)} E {mp.nstr(mx(s['E']),5)} |dY/dt| 0")
