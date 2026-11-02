import sympy as sp
# --- Model B: f=t+x^2/(2b) (double zero, no signature change, exact) in (t,x,y,z)
t,x,y,z=sp.symbols('t x y z',real=True); b,L=sp.symbols('b Lambda',positive=True)
X=[t,x,y,z]; eta=sp.diag(1,-1,-1,-1); f=t+x**2/(2*b)
df=sp.Matrix([sp.diff(f,c) for c in X]); g=eta-df*df.T
print('B det g =',sp.factor(g.det()),' g_tt=',g[0,0]); gi=g.inv().applyfunc(sp.simplify); print('B g^-1',gi.tolist())
Gam=[[[sum(gi[i,l]*(sp.diff(g[l,j],X[k])+sp.diff(g[l,k],X[j])-sp.diff(g[j,k],X[l])) for l in range(4))/2 for k in range(4)] for j in range(4)] for i in range(4)]
Ric=sp.Matrix(4,4,lambda B,C: sp.simplify(sum(sp.diff(Gam[d][B][C],X[d])-sp.diff(Gam[d][B][d],X[C])+sum(Gam[d][d][h]*Gam[h][B][C]-Gam[d][C][h]*Gam[h][B][d] for h in range(4)) for d in range(4))))
print('B Ric=0:',Ric==sp.zeros(4,4))
for k,m in [('t',t),('xi',f),('x',x),('y',y)]:
    dm=sp.Matrix([sp.diff(m,c) for c in X]); v=gi*dm   # j^a/(sqrt|g| Lambda/8piG)
    print('B j^x_%s * b/|x| ...: g^{xb}d_b m ='%k, sp.simplify(v[1]), ' times sqrt|g|=|x|/b -> ', sp.simplify(v[1]*x/b),'* sign(x)')
# --- Model C: true CP2, t=c*Psi; coordinates (r,Theta,Psi,Phi), R=1
r,T,Ps,Ph=sp.symbols('r Theta Psi Phi',positive=True); c=sp.symbols('c',positive=True)
Y=[r,T,Ps,Ph]; F=1+r**2
s=sp.zeros(4,4); s[0,0]=1/F**2; s[1,1]=r**2/(4*F)
A=r**2/(4*F**2); B_=r**2/(4*F)
s[2,2]=A; s[2,3]=s[3,2]=A*sp.cos(T); s[3,3]=A*sp.cos(T)**2+B_*sp.sin(T)**2
G=-s; G[2,2]+=c**2
Gi=G.inv().applyfunc(sp.simplify)
detG=sp.factor(sp.simplify(G.det())); print('C det g =',detG)
sInv=s.inv().applyfunc(sp.simplify); print('C s^PsiPsi =',sp.factor(sInv[2,2]))
Ga=[[[sp.simplify(sum(Gi[i,l]*(sp.diff(G[l,j],Y[k])+sp.diff(G[l,k],Y[j])-sp.diff(G[j,k],Y[l])) for l in range(4))/2) for k in range(4)] for j in range(4)] for i in range(4)]
def ric(B,C): return sum(sp.diff(Ga[d][B][C],Y[d])-sp.diff(Ga[d][B][d],Y[C])+sum(Ga[d][d][h]*Ga[h][B][C]-Ga[d][C][h]*Ga[h][B][d] for h in range(4)) for d in range(4))
Rc=sp.Matrix(4,4,lambda i,j: sp.simplify(ric(i,j)))
for i,j in [(0,2),(0,3),(1,2),(1,3)]: print('C R_',Y[i],Y[j],'=',Rc[i,j])
Rs=sp.simplify(sum(Gi[i,j]*Rc[i,j] for i in range(4) for j in range(4))); print('C R scalar =',sp.factor(Rs))
Gd=(Rc-G*Rs/2); Gu=(Gi*Gd*Gi).applyfunc(sp.simplify)
print('C G^{r Psi},G^{Theta Psi} =',Gu[0,2],Gu[1,2]); print('C g^{r Psi},g^{Theta Psi} =',Gi[0,2],Gi[1,2])
print('C G^PsiPsi =',sp.factor(Gu[2,2]))
