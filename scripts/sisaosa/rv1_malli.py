# Exact model: X^4 in M^4 x S^1 (geodesic circle of CP2), graph xi = f = a*eta + n*theta
# x=p cosh eta, t=p sinh eta, y=r cos theta, z=r sin theta.  Coordinates (p,r,eta,theta).
import sympy as sp
p,r,e,th=sp.symbols('p r eta theta',positive=True)
a,n,Lam=sp.symbols('a n Lambda',positive=True)
X=[p,r,e,th]
g=sp.Matrix([[-1,0,0,0],[0,-1,0,0],[0,0,p**2-a**2,-a*n],[0,0,-a*n,-r**2-n**2]])
D=sp.simplify(-g.det()); print('D=-det g =',sp.factor(D))
gi=g.inv().applyfunc(sp.simplify)
G3=[[[sum(gi[i,l]*(sp.diff(g[l,j],X[k])+sp.diff(g[l,k],X[j])-sp.diff(g[j,k],X[l])) for l in range(4))/2 for k in range(4)] for j in range(4)] for i in range(4)]
G3=[[[sp.simplify(c) for c in q] for q in w] for w in G3]
def ric(b,c):
    return sum(sp.diff(G3[d][b][c],X[d])-sp.diff(G3[d][b][d],X[c])+sum(G3[d][d][h]*G3[h][b][c]-G3[d][c][h]*G3[h][b][d] for h in range(4)) for d in range(4))
Ric=sp.Matrix(4,4,lambda i,j: sp.factor(sp.simplify(ric(i,j))))
Rs=sp.factor(sp.simplify(sum(gi[i,j]*Ric[i,j] for i in range(4) for j in range(4))))
print('R =',Rs)
Gd=(Ric-g*Rs/2).applyfunc(sp.simplify)
Gu=(gi*Gd*gi).applyfunc(lambda c: sp.factor(sp.simplify(c)))
for i in range(4):
    for j in range(i,4):
        print('G^',X[i],X[j],'=',Gu[i,j])
# P^{ab}*8 pi G
Pu=(Lam*gi-Gu).applyfunc(sp.simplify)
sq=sp.sqrt(D)  # D>0 side; D<0 side uses sqrt(-D): same equations since constant factor
fs={'x':p*sp.cosh(e),'t':p*sp.sinh(e),'y':r*sp.cos(th),'z':r*sp.sin(th),'xi':a*e+n*th}
for k,m in fs.items():
    dm=sp.Matrix([sp.diff(m,c) for c in X])
    j=Pu*dm
    div=sum(sp.diff(sq*j[i],X[i]) for i in range(4))
    print('div j',k,'=',sp.simplify(div/sq))
import pickle
pickle.dump((D,Rs,Gu,gi),open('/tmp/_rv1.pkl','wb')) if False else None
