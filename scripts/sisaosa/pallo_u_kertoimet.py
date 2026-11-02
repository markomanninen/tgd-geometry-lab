# Insert P = r^2 rho + om and collect the coefficients of the trace
#   E^xi = T^uu X_uu + 2 T^uw X_uw - C^u xi_u - C^w xi_w,  T = G - Lam g,  C^c = T^ab Gam^c_ab
# as polynomials in r, after clearing denominators.
import sympy as sp, pickle
d=pickle.load(open('pallo_u_yleinen.pkl','rb'))
Gam,Gu,g,gi=d['Gam'],d['Gu'],d['g'],d['gi']
r,Lam=sp.symbols('r Lam')
names=['u','v','w','wb']
n=4
rho,rw,rb,rwb,rww,rbb=sp.symbols('rho rho_w rho_wb rho_wwb rho_ww rho_wbwb')
om,ou,ow,ob,ouu,ouw,oub,owb,oww,obb=sp.symbols('om om_u om_w om_wb om_uu om_uw om_uwb om_wwb om_ww om_wbwb')
sy=lambda s: sp.Symbol(s)
Psub={sy('P'):r**2*rho+om, sy('P_v'):r*rho, sy('P_vv'):rho/2, sy('P_u'):-r*rho+ou, sy('P_uu'):rho/2+ouu,
      sy('P_uv'):-rho/2, sy('P_w'):r**2*rw+ow, sy('P_wb'):r**2*rb+ob, sy('P_vw'):r*rw, sy('P_vwb'):r*rb,
      sy('P_uw'):-r*rw+ouw, sy('P_uwb'):-r*rb+oub, sy('P_wwb'):r**2*rwb+owb,
      sy('P_ww'):r**2*rww+oww, sy('P_wbwb'):r**2*rbb+obb, sy('P_uvw'):-rw/2}
T=(Gu-Lam*gi)
Tp=T.applyfunc(lambda e:e.subs(Psub))
Gp=[[[Gam[c][a][b].subs(Psub) for b in range(n)] for a in range(n)] for c in range(n)]
C=[sum(Tp[a,b]*Gp[c][a][b] for a in range(n) for b in range(n)) for c in range(n)]
Phi=r**2*rho+om
res={}
for nm,e in [('Tuu',Tp[0,0]),('Tuw',Tp[0,2]),('Cu',C[0]),('Cw',C[2]),('Cwb',C[3])]:
    q=sp.cancel(sp.together(e))
    res[nm]=q
    a,b=sp.fraction(q)
    bf=sp.factor(b)
    print(nm,'denominator',bf)
    pa=sp.Poly(a,r)
    for (k,),co in pa.terms():
        print('   r^%d:'%k,sp.factor(co))
pickle.dump(res,open('pallo_u_kertoimet.pkl','wb'))
