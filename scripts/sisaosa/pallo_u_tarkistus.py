# Compare the general formula with the library values, and check the reduction steps.
import sympy as sp, pickle
res=pickle.load(open('pallo_u_kertoimet.pkl','rb'))
u,w,wb,r,Lam=sp.symbols('u w wb r Lam')
I=sp.I
S={'uw':(u*w,0,u*wb,0),'wpu':(w+u,0,wb+u,0),'w2pu':(w**2+u,0,wb**2+u,0),'w_uw':(w,u*w,wb,u*wb),
   'rot':((1+I*u)/(1-I*u)*w,0,(1-I*u)/(1+I*u)*wb,0),'u_only':(u,0,u,0),'rank2':(w+u*w**2,u**2,wb+u*wb**2,u**2)}
rho=4/(1+w*wb)**2
def data(x1,x2,y1,y2):
    x=[sp.sympify(x1),sp.sympify(x2)]; y=[sp.sympify(y1),sp.sympify(y2)]
    D=1+x[0]*y[0]+x[1]*y[1]
    hh=lambda a,b: sum((sp.Integer(k==l)/D-y[k]*x[l]/D**2)*a[k]*b[l] for k in range(2) for l in range(2))
    xu=[sp.diff(e,u) for e in x]; xw=[sp.diff(e,w) for e in x]
    yu=[sp.diff(e,u) for e in y]; yb=[sp.diff(e,wb) for e in y]
    A=hh(xu,yu); B=hh(xw,yu); Bb=hh(xu,yb); om=hh(xw,yb)
    G=lambda p,q,k: -(sp.Integer(k==0)*0+ (p[k]*sum(y[j]*q[j] for j in range(2))+q[k]*sum(y[j]*p[j] for j in range(2)))/D)
    Xuu=[sp.diff(x[k],u,2)+G(xu,xu,k) for k in range(2)]
    Xuw=[sp.diff(x[k],u,w)+G(xu,xw,k) for k in range(2)]
    return dict(x=x,y=y,xu=xu,xw=xw,yu=yu,yb=yb,A=A,B=B,Bb=Bb,om=om,Xuu=Xuu,Xuw=Xuw,hh=hh)
def subs_tab(d):
    t={}
    v=[('u',u),('w',w),('wb',wb)]
    A,B,Bb,om=d['A'],d['B'],d['Bb'],d['om']
    sy=sp.Symbol
    t[sy('rho')]=rho; t[sy('rho_w')]=sp.diff(rho,w); t[sy('rho_wb')]=sp.diff(rho,wb)
    t[sy('om')]=om
    for nm,e in [('om',om),('A',A),('B',B),('Bb',Bb)]:
        t[sy(nm)]=e
        for a,x in v:
            t[sy(nm+'_'+a)]=sp.diff(e,x)
            for b,y in v:
                t[sy(nm+'_'+a+b)]=sp.diff(e,x,y)
                t[sy(nm+'_'+b+a)]=sp.diff(e,x,y)
    return t
rows={}
for l in open('pallo_u_max2.out'):
    p=l.split(); rows.setdefault(p[1],[]).append([sp.Rational(s.replace('(','').replace(')','').replace('--','')) for s in p[2:6]]+[float(s) for s in p[6:]])
import mpmath as mp
mp.mp.dps=30
worst=0
R=sp.Symbol('r')
for nm,(a,b,c,dd) in S.items():
    if nm not in rows: continue
    d=data(a,b,c,dd); t=subs_tab(d)
    f=[res[q].subs(t) for q in ('Tuu','Tuw','Cu','Cw')]
    Ls=sp.Symbol('Lam')
    for k in (0,1):
        E=f[0]*d['Xuu'][k]+2*f[1]*d['Xuw'][k]-f[2]*d['xu'][k]-f[3]*d['xw'][k]
        Gf=sp.lambdify((u,w,wb,R),E.subs(Ls,0),'mpmath'); Hf=sp.lambdify((u,w,wb,R),sp.diff(E,Ls)*(-1),'mpmath')
        for row in rows[nm]:
            U,V,sa,sb=[mp.mpf(int(x.p))/int(x.q) for x in row[:4]]
            p=(U,mp.mpc(sa,sb),mp.mpc(sa,-sb),(V-U)/2)
            mH=complex(row[4+2*k],row[5+2*k]); mG=complex(row[8+2*k],row[9+2*k])
            e1=abs(complex(Hf(*p))-mH); e2=abs(complex(Gf(*p))-mG); worst=max(worst,e1,e2)
            if k==0 and row is rows[nm][0]:
                print(nm,'H',complex(Hf(*p)),mH,'GB',complex(Gf(*p)),mG,flush=True)
print('largest difference formula vs library',worst)
