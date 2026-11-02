# Validation: the jet evaluator against the library values of pallo_u_max2.out.
from pallo_uv_lib import *
import sympy as sp
rows=[l.split() for l in open('pallo_u_max2.out') if l.startswith('ROW')]
surf={'uw':lambda u,w:(u*w,J.const(0)),'wpu':lambda u,w:(w+u,J.const(0)),'w2pu':lambda u,w:(w*w+u,J.const(0)),
      'w_uw':lambda u,w:(w,u*w),'u_only':lambda u,w:(u,J.const(0))}
worst=[0,0]; cnt=0
def fl(s): return mp.mpf(str(s))
for p in rows:
    nm=p[1]
    if nm not in surf: continue
    q=[sp.Rational(s.replace('(','').replace(')','').replace('--','')) for s in p[2:6]]
    U,V,sa,sb=[mp.mpf(int(x.p))/int(x.q) for x in q]
    u=J.var(0,U); v=J.var(1,V); a=J.var(2,sa); b=J.var(3,sb)
    w=a+b*mp.mpc(0,1); wb=a-b*mp.mpc(0,1)
    x=sph_chart(u,v,w,wb); z=surf[nm](u,w)
    S=surface(x,list(z))
    # the output columns are real and imaginary parts of H^xi1 components: Re, Im of x1, Re, Im of y1
    H1=[mp.re(S['H'][4]),mp.im(S['H'][4])]; E1=[mp.re(S['E'][4]),mp.im(S['E'][4])]
    lib=[float(s) for s in p[6:]]
    e1=max(abs(H1[0]-lib[0]),abs(H1[1]-lib[1])); e2=max(abs(E1[0]-lib[4]),abs(E1[1]-lib[5]))
    worst=[max(worst[0],e1),max(worst[1],e2)]; cnt+=1
print('points',cnt,'largest difference from the library: H',mp.nstr(worst[0],4),' G^abB_ab',mp.nstr(worst[1],4))
