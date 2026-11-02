# Flux of M^4 translation charge into the cut-off surface r -> rho=w(r), with and without the
# Gibbons-Hawking-York term, on both sides of D=0, for two foliations. Units 8 pi G = 1, Lambda kept.
import sympy as sp, mpmath as mp
mp.mp.dps=60
p,r,e,th=sp.symbols('p r eta theta',positive=True)
a,n,Lam=sp.symbols('a n Lambda',positive=True)
X=[p,r,e,th]
ghat=-sp.Matrix([[-1,0,0,0],[0,-1,0,0],[0,0,p**2-a**2,-a*n],[0,0,-a*n,-r**2-n**2]])   # mostly plus
gi=ghat.inv().applyfunc(sp.simplify)
Gam=[[[sp.simplify(sum(gi[i,l]*(sp.diff(ghat[l,j],X[k])+sp.diff(ghat[l,k],X[j])-sp.diff(ghat[j,k],X[l])) for l in range(4))/2) for k in range(4)] for j in range(4)] for i in range(4)]
D=p**2*(n**2+r**2)-a**2*r**2
Gu=sp.zeros(4,4)  # G^{ab}[g]=G^{ab}[ghat]; from rv1
Gu[0,0]=n**2*p**2*(p**2-a**2)/D**2; Gu[0,1]=Gu[1,0]=-a**2*n**2*p*r/D**2
Gu[1,1]=-a**2*r**2*(n**2+r**2)/D**2; Gu[2,2]=-n**2*p**2/D**2; Gu[3,3]=-a**2*r**2/D**2
gu=-gi  # inverse of g mostly minus
w=sp.Function('w')(r)
sub={p:w}
Y=[w,r,e,th]; yy=[r,e,th]
E=sp.Matrix(3,4,lambda i,j: sp.diff(Y[j],yy[i]))
gh=ghat.subs(sub)
h=(E*gh*E.T)
hi=h.inv()
s=sp.Symbol('s')          # s=+1 if normal points to +rho, -1 otherwise
wp=sp.diff(w,r)
Nc=[s/sp.sqrt(1+wp**2),-s*wp/sp.sqrt(1+wp**2),0,0]   # covector, unit in ghat
K=sp.zeros(3,3)
for i in range(3):
  for j in range(3):
    t=0
    for c in range(4):
      if Nc[c]==0: continue
      t+=-Nc[c]*(sp.diff(Y[c],yy[i],yy[j])+sum(Gam[c][q][u].subs(sub)*E[i,q]*E[j,u] for q in range(4) for u in range(4)))
    K[i,j]=t
Kt=sum(hi[i,j]*K[i,j] for i in range(3) for j in range(3))
Pi=(Kt*hi-hi*K*hi)
sig=sp.Symbol('sig')  # sig=sign of det ghat-side: det h = sig*|det h|
deth=h.det()
sqh=sp.sqrt(sig*deth)
mf={'x':(w*sp.cosh(e),p*sp.cosh(e)),'t':(w*sp.sinh(e),p*sp.sinh(e)),'y':(r*sp.cos(th),r*sp.cos(th)),'z':(r*sp.sin(th),r*sp.sin(th))}
out={}
for k,(mY,m4) in mf.items():
    dm4=[sp.diff(m4,c) for c in X]
    fluxL=sum(Nc[b]*gu[a,b].subs(sub)*dm4[a].subs(sub) for a in range(4) for b in range(2))*sqh*Lam
    fluxG=-sum(Nc[b]*Gu[a,b].subs(sub)*dm4[a].subs(sub) for a in range(4) for b in range(2))*sqh
    dm=[sp.diff(mY,c) for c in yy]
    A=[sqh*sum(Pi[i,j]*dm[j] for j in range(3)) for i in range(3)]
    surf=-sum(sp.diff(A[i],yy[i]) for i in range(3))
    out[k]=(fluxL,fluxG,surf)
vals={e:mp.mpf('0.7'),th:mp.mpf('0.4')}
def ev(expr,W,rv,A,N,Lv,sv,sg):
    # replace derivatives of w by numerical values
    d=[W(rv,i) for i in range(5)]
    ex=expr
    for i in range(4,0,-1):
        ex=ex.subs(sp.Derivative(w,(r,i)) if i>1 else sp.Derivative(w,r),sp.Float(str(d[i]),55))
    ex=ex.subs(w,sp.Float(str(d[0]),55)).subs({r:sp.Float(str(rv),55),a:sp.Float(str(A),55),n:sp.Float(str(N),55),Lam:sp.Float(str(Lv),55),s:sv,sig:sg,e:sp.Float('0.7',55),th:sp.Float('0.4',55)})
    return mp.mpf(str(sp.N(ex,50)))
A,N,Lv=mp.mpf(1),mp.mpf('0.8'),mp.mpf('0.3'); rv=mp.mpf('1.1')
def foliation(kind,dl):
    if kind=='D':
        fn=lambda x: mp.sqrt((dl+A*A*x*x)/(N*N+x*x))
    else:
        fn=lambda x: mp.sqrt((A*A*x*x)/(N*N+x*x))+dl
    return lambda x,i: mp.diff(fn,x,i) if i else fn(x)
print('# a=1,n=0.8,Lambda=0.3,r=1.1,eta=0.7,theta=0.4, 8piG=1')
print('# side delta | flux(L) flux(G) surface(GHY) total=flux+surface for k=x,t,y,z')
print('rho_Sigma=',mp.nstr(mp.sqrt(A*A*rv**2/(N*N+rv**2)),8))
for kind in ['D','rho']:
  for sgn,name,sv,sg in [(1,'Mink',-1,-1),(-1,'Eukl',1,1)]:
    for dl in ['1e-2','1e-4','1e-6','1e-8']:
        d=sgn*mp.mpf(dl)
        W=foliation(kind,d)
        row=[]
        for k in 'xtyz':
            fl,fg,su=out[k]
            FL=ev(fl,W,rv,A,N,Lv,sv,sg);FG=ev(fg,W,rv,A,N,Lv,sv,sg);SU=ev(su,W,rv,A,N,Lv,sv,sg)
            row.append((FL,FG,SU))
        print(kind,name,dl,' | '.join(f"{k}: L {mp.nstr(q[0],6)} G {mp.nstr(q[1],6)} S {mp.nstr(q[2],6)} T {mp.nstr(q[0]+q[1]+q[2],6)}" for k,q in zip('xtyz',row)))
