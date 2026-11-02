# Sign checks of the quadratic action and of the leading bulk coefficient.
import sympy as sp
t=sp.symbols('t',real=True)
def scal(g,xs):
    n=len(xs); gi=g.inv()
    Gam=[[[sum(gi[i,l]*(sp.diff(g[l,j],xs[k])+sp.diff(g[l,k],xs[j])-sp.diff(g[j,k],xs[l])) for l in range(n))/2 for k in range(n)] for j in range(n)] for i in range(n)]
    Ric=sp.zeros(n)
    for j in range(n):
        for k in range(n):
            Ric[j,k]=sum(sp.diff(Gam[i][j][k],xs[i]) for i in range(n))-sum(sp.diff(Gam[i][j][i],xs[k]) for i in range(n))+sum(Gam[i][i][l]*Gam[l][j][k]-Gam[i][k][l]*Gam[l][j][i] for i in range(n) for l in range(n))
    return Ric,sum(gi[i,j]*Ric[i,j] for i in range(n) for j in range(n)),gi
# Clifford torus rho(t) in S^3: H=0, K_h=0, |A|^2=2
x,al,be=sp.symbols('x al be',real=True); rho=sp.Function('rho')(t); N=sp.Function('N')(t)
g=sp.diag(N**2,-1,-sp.cos(rho)**2,-sp.sin(rho)**2)
_,R,_=scal(g,[t,x,al,be])
sq=N*sp.cos(rho)*sp.sin(rho)
K=sp.diff(rho,t)*(sp.cos(rho)/sp.sin(rho)-sp.sin(rho)/sp.cos(rho))/N
L1=-2*sp.diff(rho,t)**2*sp.cos(rho)*sp.sin(rho)/N
X=2*sp.cos(rho)*sp.sin(rho)*K
res=sp.simplify(sq*R-L1+sp.diff(X,t)); res2=sp.simplify(sq*R-L1-sp.diff(X,t))
print('Clifford: sqrt g R - L1 -+ dX/dt =',res,'|',res2)
# sphere dilation
r=sp.Function('r')(t); th,ph=sp.symbols('th ph',real=True)
g=sp.diag(N**2,-1,-r**2,-r**2*sp.sin(th)**2)
_,R,_=scal(g,[t,x,th,ph])
sq=N*r**2
L1=-2*N+2*sp.diff(r,t)**2/N; X=4*r*sp.diff(r,t)/N
print('Sphere: ',sp.simplify(sq*R-L1+sp.diff(X,t)),'|',sp.simplify(sq*R-L1-sp.diff(X,t)))
# leading coefficient of G^y_y for g_tt=n^a with c=1+c1 n
n,c1,y,z=sp.symbols('n c1 y z',positive=True); a=sp.symbols('a',positive=True)
Nn=n**(a/2); c=1+c1*n
g=sp.diag(Nn**2,-1,-c**2,-c**2)
Ric,R,gi=scal(g,[t,n,y,z])
Gyy=sp.simplify(gi[2,2]*Ric[2,2]-R/2)
print('n^2 G^y_y at n->0:',sp.simplify(sp.limit(sp.simplify(n**2*Gyy),n,0)))
