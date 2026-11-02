# Numerical check of the scalar conditions S1, S2 as combinations of c4..c0.
import sympy as sp, pickle, mpmath as mp
exec(open('pallo_u_tarkistus.py').read().split("rows={}")[0])
mp.mp.dps=30
Sx={'gen':(w+u*w**2,u**2+w*u/3,wb+u*wb**2,u**2+wb*u/3),'w_uw':S['w_uw'],'rot':S['rot']}
pv=[(mp.mpf(1)/3,mp.mpc(2/7,-.6),mp.mpc(2/7,.6)),(mp.mpf(-1)/2,mp.mpc(.25,.125),mp.mpc(.25,-.125))]
worst=0
for nm,(a,b,c,dd) in Sx.items():
    d=data(a,b,c,dd); A,B,Bb,om=d['A'],d['B'],d['Bb'],d['om']
    Y=A-1; q=om*sp.diff(rho,wb)-sp.diff(om,wb)*rho
    Bbu,Bbw,Ab,omu=sp.diff(Bb,u),sp.diff(Bb,w),sp.diff(A,wb),sp.diff(om,u)
    Bbwb=sp.diff(Bb,w,wb); omb=sp.diff(om,wb); rb=sp.diff(rho,wb)
    for k in (0,1):
        Xuu,Xuw,xu,xw=d['Xuu'][k],d['Xuw'][k],d['xu'][k],d['xw'][k]
        R4=om*Xuu+Bb*Xuw+omu*xu+Bbu*xw
        R3=2*rho*q*Xuw+rho**3*(om*Y*xu+(Bb*Y-2*sp.diff(Bbw/rho,wb))*xw)
        R2=4*om**2*rho*Xuu+2*rho*om*omu*xu+(4*Y*q+2*rho*om*Ab-6*rho*Bb*Bbw)*xw
        R1=2*om*q*Xuw+om**2*rho**2*Y*xu-(Bb*om*rho**2*Y+2*om*rb*Bbw-4*rho*omb*Bbw+2*om*rho*Bbwb)*xw
        R0=om**2*Xuu-Bb*om*Xuw+(Ab*om+Bb*Bbw-Bbu*om)*xw
        e1=om*R3-rho*R1-(2*rho**3*om*Bb*Y+4*rho*q*Bbw)*xw
        V1=om*R4-R0; V2=R2/(4*rho)-R0
        e2=2*V2-V1-(2*Y*q/rho-4*Bb*Bbw)*xw
        f=sp.lambdify((u,w,wb),[e1,e2],'mpmath')
        for p in pv:
            worst=max(worst,*[abs(x) for x in f(*p)])
print('largest residual of S1, S2 combinations',worst)
