# Explicit check: CP2-type extremal with interior action sqrt|g|(c_V + c_R R).
# Eguchi-Hanson chart of CP2, project normalisation Ric = 6 s / R^2.
# ds^2/R^2 = dr^2/F^2 + r^2/(4F^2)(dPsi+cos(Th)dPhi)^2 + r^2/(4F)(dTh^2+sin^2 Th dPhi^2), F=1+r^2
import sympy as sp
r,Th,Psi,Phi=sp.symbols('r Theta Psi Phi',positive=True)
R=sp.symbols('R',positive=True)
X=[r,Th,Psi,Phi]
F=1+r**2
def cp2():
    a=r**2/(4*F**2); b=r**2/(4*F); c=sp.cos(Th); s_=sp.sin(Th)
    m=sp.zeros(4)
    m[0,0]=1/F**2; m[1,1]=b
    m[2,2]=a; m[2,3]=m[3,2]=a*c; m[3,3]=a*c**2+b*s_**2
    return m*R**2
def curv(g,X,simp=sp.simplify):
    n=len(X); gi=g.inv().applyfunc(simp)
    Gam=[[[simp(sum(gi[a,d]*(sp.diff(g[d,b],X[c])+sp.diff(g[d,c],X[b])-sp.diff(g[b,c],X[d])) for d in range(n))/2)
           for c in range(n)] for b in range(n)] for a in range(n)]
    Ric=sp.zeros(n)
    for b in range(n):
        for c in range(b,n):
            e=0
            for a in range(n):
                e+=sp.diff(Gam[a][b][c],X[a])-sp.diff(Gam[a][b][a],X[c])
                for d in range(n):
                    e+=Gam[a][a][d]*Gam[d][b][c]-Gam[a][c][d]*Gam[d][b][a]
            Ric[b,c]=Ric[c,b]=simp(e)
    return gi,Gam,Ric
s=cp2()
print('det s =',sp.factor(sp.simplify(s.det())))
gi_s,_,Ric_s=curv(s,X)
print('Ric(s)-6/R^2 s =',(Ric_s-6/R**2*s).applyfunc(sp.simplify))
# signature (+,-,-,-) on H: induced metric with null m^k(Psi) is g=-s
g=-s
gi,_,Ric=curv(g,X)
Rs=sp.simplify(sum(gi[i,j]*Ric[i,j] for i in range(4) for j in range(4)))
G=(Ric-g*Rs/2).applyfunc(sp.simplify)
print('Ric(g)-Ric(s) =',(Ric-Ric_s).applyfunc(sp.simplify))
print('scalar R(g) =',Rs)
print('G_ab - (6/R^2) g_ab =',(G-6/R**2*g).applyfunc(sp.simplify))
# induced metric: m^k(u) with u a CP2 function: g_ab = -s_ab + q(u) du_a du_b, q = mdot.mdot
L,A,w=sp.symbols('L A omega',positive=True)
u=Psi
m=sp.Matrix([sp.sqrt(L**2)*u,A*sp.cos(w*u),A*sp.sin(w*u),sp.sqrt(L**2-A**2*w**2)*u])
eta=sp.diag(1,-1,-1,-1)
md=m.diff(u)
q=sp.simplify((md.T*eta*md)[0])
print('mdot^2 for helix m(u)=',q)
gind=-s+sp.Matrix(4,4,lambda a,b:q*(1 if (a==2 and b==2) else 0))
print('induced minus (-s):',(gind+s).applyfunc(sp.simplify))
# Box_g of a function f: (1/sqrt g) d_a(sqrt g g^ab d_b f)
sq=r**3*sp.sin(Th)/(8*F**3)*R**4
def box(f):
    return sp.simplify(sum(sp.diff(sq*gi[a,b]*sp.diff(f,X[b]),X[a]) for a in range(4) for b in range(4))/sq)
print('Box_g Psi =',box(Psi),'  |dPsi|^2_s =',sp.simplify(gi_s[2,2]))
print('Box_g m^1 (helix) =',sp.simplify(box(m[1])))
print('Box_g r =',box(r))
rho=sp.atan(r)
print('Box_g rho (geodesic distance/R) =',box(rho))
# radial harmonic function u(rho): u' A(rho)=const, A=2 pi^2 sin^3 cos
rh=sp.symbols('rho',positive=True)
Afun=2*sp.pi**2*sp.sin(rh)**3*sp.cos(rh)
print('level volume / R^3 =',Afun,' integral =',sp.integrate(Afun,(rh,0,sp.pi/2)))
print('max at tan^2 rho=3 :',sp.N(Afun.subs(rh,sp.pi/3)))
# radial harmonic: u'(r)= 1/(sq-weight * g^rr) ; verify Box=0, in r
U=sp.Function('U')
ur=sp.integrate(sp.simplify(F**3/r**3/F**2),r)
print('u(r)=',ur,'  Box_g u =',box(ur))
print('dudr =',sp.simplify(sp.diff(ur,r)))
# flux of grad u through r=const, measure dTh dPsi dPhi (units where dt/du=L, length R)
fl=sp.integrate(sp.integrate(sp.integrate(sp.simplify(sq*(-gi[0,0])*sp.diff(ur,r)),(Th,0,sp.pi)),(Psi,0,4*sp.pi)),(Phi,0,2*sp.pi))
print('flux of s^{rb}d_b u =',sp.simplify(fl),' (r independent if Box=0)')
