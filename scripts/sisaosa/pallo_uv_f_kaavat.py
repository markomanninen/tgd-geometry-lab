# (1) closed CP_1 formula for H^xi.  (2) first order of the moving vertex.
from pallo_uv_lib import *
I=mp.mpc(0,1); hf=mp.mpf(1)/2
for p,c in [((0.3,1.1,-0.7,0.5),mp.mpf('0.7')),((-0.4,0.6,1.3,-0.9),mp.mpf('0.4'))]:
    t,x,y,z=[J.var(i,p[i]) for i in range(4)]
    r=(x*x+y*y+z*z).sqrt(); w=(x+y*I)/(r+z); u=t-r
    xi=(u*I).exp()*w*w/r*c + w*(0.2); xb=xi.conj()
    A=(1+xi*xb).inv(); h=A*A
    Pp=dot(xi,xi); Pb=dot(xb,xb); cc=dot(xi,xb)
    ka=1-h*cc*hf; Dd=ka*ka-h*h*Pp*Pb*(mp.mpf(1)/4); sD=Dd.sqrt()
    V=[(ka*(xi.d(i))+h*Pp*(xb.d(i))*hf)*sD.inv()*ETA[i] for i in range(4)]
    div=sum((V[i].d(i).v() for i in range(4)))
    lhs=div/sD.v()-2*xb.v()*Pp.v()*A.v()/Dd.v()
    S=surface([t,x,y,z],[xi,J.const(0)])
    print('closed formula',mp.nstr(lhs,12),'evaluator',mp.nstr(S['H'][4],12),'P',mp.nstr(abs(Pp.v()),5))
print('moving vertex, first order: r(Y-w) against -(d_+ - 2 d_z w - d_- w^2)/2, d=(e sin u,0,0)')
for e in (mp.mpf('1e-3'),mp.mpf('1e-5')):
    p=(0.3,1.1,-0.7,0.5); T,X,Y0,Z=[mp.mpf(q) for q in p]
    tt=mp.re(mp.findroot(lambda s:(T-s)-mp.sqrt((X-e*mp.sin(s))**2+Y0**2+Z**2),T-1.4))
    dx=X-e*mp.sin(tt); Yv=(dx+Y0*I)/((T-tt)+Z)
    r=mp.sqrt(X**2+Y0**2+Z**2); w=(X+Y0*I)/(r+Z); u=T-r
    d=e*mp.sin(u); pred=-(d-d*w**2)/2
    print(e,mp.nstr((r*(Yv-w))/e,10),mp.nstr(pred/e,10))
