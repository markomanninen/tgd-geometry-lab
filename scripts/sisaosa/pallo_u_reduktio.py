# Check the hand-reduced coefficients c4..c0 of Phi^4 E^xi (Lam=0), the scalar conditions S1, S2,
# the curvature identity, and print the r^4 condition for the four examples with generic f, g.
import sympy as sp, pickle, random
exec(open('pallo_u_tarkistus.py').read().split("rows={}")[0])
sy=sp.Symbol
pts=[{u:sp.Rational(1,3),w:sp.Rational(2,7)-sp.Rational(3,5)*I,wb:sp.Rational(2,7)+sp.Rational(3,5)*I},
     {u:-sp.Rational(1,2),w:sp.Rational(1,4)+I/8,wb:sp.Rational(1,4)-I/8}]
Rs=[sp.Rational(a,7) for a in (3,5,9,13,17,23)]
Sx=dict(S); Sx['gen']=(w+u*w**2,u**2+w*u/3,wb+u*wb**2,u**2+wb*u/3)
import mpmath as mp
mp.mp.dps=30
worst=0; worst2=0
pv=[(mp.mpf(1)/3,mp.mpc(2/7,-.6),mp.mpc(2/7,.6)),(mp.mpf(-1)/2,mp.mpc(.25,.125),mp.mpc(.25,-.125))]
for nm,(a,b,c,dd) in Sx.items():
    d=data(a,b,c,dd); t=subs_tab(d)
    A,B,Bb,om=d['A'],d['B'],d['Bb'],d['om']
    Y=A-1; q=om*sp.diff(rho,wb)-sp.diff(om,wb)*rho
    Bbu,Bbw,Ab,omu=sp.diff(Bb,u),sp.diff(Bb,w),sp.diff(A,wb),sp.diff(om,u)
    Bbwb=sp.diff(Bb,w,wb); omb=sp.diff(om,wb); rb=sp.diff(rho,wb)
    L=lambda e: sp.lambdify((u,w,wb,sp.Symbol('r')),sp.sympify(e),'mpmath')
    f=[res[q_].subs(sy('Lam'),0).subs(t) for q_ in ('Tuu','Tuw','Cu','Cw')]
    for k in (0,1):
        Xuu,Xuw,xu,xw=d['Xuu'][k],d['Xuw'][k],d['xu'][k],d['xw'][k]
        c4=-2*rho**3*(om*Xuu+Bb*Xuw+omu*xu+Bbu*xw)
        c3=2*(2*rho*q*Xuw+rho**3*(om*Y*xu+(Bb*Y-2*sp.diff(Bbw/rho,wb))*xw))
        c2=-(4*om**2*rho**2*Xuu+2*rho**2*om*omu*xu+rho*(4*Y*q+2*rho*om*Ab-6*rho*Bb*Bbw)*xw)
        c1=2*(2*om*q*Xuw+om**2*rho**2*Y*xu-(Bb*om*rho**2*Y+2*om*rb*Bbw-4*rho*omb*Bbw+2*om*rho*Bbwb)*xw)
        c0=-2*om*rho*(om**2*Xuu-Bb*om*Xuw+(Ab*om+Bb*Bbw-Bbu*om)*xw)
        R=sp.Symbol('r')
        Phi=R**2*rho+om
        E=L((f[0]*Xuu+2*f[1]*Xuw-f[2]*xu-f[3]*xw)*Phi**4)
        pred=L(c4*R**4+c3*R**3+c2*R**2+c1*R+c0)
        rel=L(omu-Bbw-sp.diff(B,wb))
        for p in pv:
            worst2=max(worst2,abs(rel(*p,0)))
            for r0 in (mp.mpf(3)/7,mp.mpf(9)/7,mp.mpf(23)/7):
                worst=max(worst,abs(E(*p,r0)-pred(*p,r0)))
    y=d['y'];yu=d['yu'];yb=d['yb'];D=1+d['x'][0]*y[0]+d['x'][1]*y[1]
    Gb=lambda p,q_,k: -(p[k]*sum(d['x'][j]*q_[j] for j in range(2))+q_[k]*sum(d['x'][j]*p[j] for j in range(2)))/D
    Yub=[sp.diff(y[k],u,wb)+Gb(yu,yb,k) for k in range(2)]
    hX=d['hh'](d['Xuw'],Yub)
    kn=L(hX-sp.diff(A,w,wb)); kd=L(om*A+B*Bb)
    print(nm,'kappa',[mp.nstr(kn(*p,0)/kd(*p,0),10) if abs(kd(*p,0))>1e-20 else 'degenerate' for p in pv],flush=True)
print('largest difference c4..c0 vs raw formula',worst,' relation om_u',worst2,flush=True)
# examples with generic functions
f=sp.Function('f')(u);fb=sp.Function('fb')(u);g=sp.Function('g')(u);gb=sp.Function('gb')(u)
for nm,(a,b,c,dd) in {'f w':(f*w,0,fb*wb,0),'w+g':(w+g,0,wb+gb,0),'w^2+g':(w**2+g,0,wb**2+gb,0),'w,g w':(w,g*w,wb,gb*wb)}.items():
    d=data(a,b,c,dd);A,B,Bb,om=d['A'],d['B'],d['Bb'],d['om']
    print('---',nm)
    print(' om=',sp.factor(om)); print(' A =',sp.factor(A)); print(' Bb=',sp.factor(Bb))
    for k in (0,1):
        e=om*d['Xuu'][k]+Bb*d['Xuw'][k]+sp.diff(om,u)*d['xu'][k]+sp.diff(Bb,u)*d['xw'][k]
        print(' r^4 comp',k+1,'=',sp.factor(sp.together(e)))
