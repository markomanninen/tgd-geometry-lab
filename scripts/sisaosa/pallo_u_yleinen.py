# General ansatz: spherical H-J, xi^k(u,w).  Metric in (u,v,w,wb):
#   ds2 = du dv - A du^2 - P dw dwb - B du dw - Bb du dwb
# P(u,v,w,wb) kept generic (later P = (v-u)^2/4 rho + om), A,B,Bb functions of (u,w,wb),
# A = h(xi_u,xib_u), B = h(xi_w,xib_u), Bb = h(xi_u,xib_wb), om = h(xi_w,xib_wb).
# Derivative atoms are replaced by plain symbols before cancelling, which keeps it fast.
import sympy as sp, pickle
u,v,w,wb=sp.symbols('u v w wb')
X=[u,v,w,wb]
P=sp.Function('P')(u,v,w,wb)
A=sp.Function('A')(u,w,wb); B=sp.Function('B')(u,w,wb); Bb=sp.Function('Bb')(u,w,wb)
h=sp.Rational(1,2)
g=sp.Matrix([[-A,h,-B/2,-Bb/2],[h,0,0,0],[-B/2,0,0,-P/2],[-Bb/2,0,-P/2,0]])
gi=sp.Matrix([[0,2,0,0],[2,4*(A-B*Bb/P),-2*Bb/P,-2*B/P],[0,-2*Bb/P,0,-2/P],[0,-2*B/P,-2/P,0]])
assert (g*gi).applyfunc(sp.simplify)==sp.eye(4)
n=4
Gam=[[[sum(gi[c,d]*(sp.diff(g[d,a],X[b])+sp.diff(g[d,b],X[a])-sp.diff(g[a,b],X[d])) for d in range(n))/2
       for b in range(n)] for a in range(n)] for c in range(n)]
def ric(a,b):
    s=0
    for c in range(n):
        s+=sp.diff(Gam[c][a][b],X[c])-sp.diff(Gam[c][a][c],X[b])
        for d in range(n):
            s+=Gam[c][c][d]*Gam[d][a][b]-Gam[c][b][d]*Gam[d][a][c]
    return s
Ric=sp.zeros(n,n)
for a in range(n):
    for b in range(a,n):
        Ric[a,b]=ric(a,b).doit(); Ric[b,a]=Ric[a,b]
# atoms -> symbols
ats=set()
for e in list(Ric)+[Gam[c][a][b] for c in range(n) for a in range(n) for b in range(n)]:
    ats|=e.atoms(sp.Derivative)
ats=sorted(ats,key=lambda d:-d.derivative_count)
tab={}
for d in ats:
    nm=str(d.expr.func)+'_'+''.join(str(x)*k for x,k in d.variable_count)
    tab[d]=sp.Symbol(nm)
base={P:sp.Symbol('P'),A:sp.Symbol('A'),B:sp.Symbol('B'),Bb:sp.Symbol('Bb')}
def S(e):
    e=e.xreplace(tab).xreplace(base)
    return e
RicS=Ric.applyfunc(lambda e: sp.cancel(S(e)))
gS=g.applyfunc(S); giS=gi.applyfunc(S)
GamS=[[[sp.cancel(S(Gam[c][a][b])) for b in range(n)] for a in range(n)] for c in range(n)]
R=sp.cancel(sum(giS[a,b]*RicS[a,b] for a in range(n) for b in range(n)))
Gl=RicS-R/2*gS
Gu=(giS*Gl*giS).applyfunc(sp.factor)
pickle.dump(dict(Gam=GamS,Ric=RicS,R=R,Gu=Gu,g=gS,gi=giS),open('pallo_u_yleinen.pkl','wb'))
names=['u','v','w','wb']
print('R =',sp.factor(R))
for a in range(n):
    for b in range(a,n):
        print('Ric_',names[a],names[b],'=',sp.factor(RicS[a,b]))
for a in range(n):
    for b in range(a,n):
        print('G^',names[a],names[b],'=',Gu[a,b])
