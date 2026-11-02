# Local double-zero analysis for the volume equation d_a(f^a/sqrt|F|)=0, f=t+A(t)x^2/2+..., and K-C-S identity checks
import sympy as sp
t,x=sp.symbols('t x'); x_=sp.symbols('x_',positive=True)
A=sp.Function('A')(t); c0=sp.symbols('c0',positive=True)
f=t+A*x**2/2
F=sp.diff(f,t)**2-sp.diff(f,x)**2-1
print('F =',sp.series(F,x,0,4).removeO())
for sgn,name in [(1,'Eukl F>0'),(-1,'Mink F<0')]:
    root=sp.sqrt(sgn*F.subs(x,x_))
    eom=(sp.diff(sp.diff(f,t).subs(x,x_)/root,t)-sp.diff(sp.diff(f,x).subs(x,x_)/root,x_))
    # leading term with A' = sgn*c0 + A^2 ... substitute derivatives
    Ap=A**2+sgn*c0
    App=sp.diff(Ap,t).subs(sp.Derivative(A,t),Ap)
    e2=eom.subs(sp.Derivative(A,(t,2)),App).subs(sp.Derivative(A,t),Ap)
    e3=sp.simplify(e2.subs(A,sp.Symbol('a'))*x_)
    print(name,'x*EOM as x->0 =',sp.limit(e3,x_,0,'+'))
a=sp.sqrt(c0)
print('Eukl solution check',sp.simplify(sp.diff(a*sp.tan(a*t),t)-(a*sp.tan(a*t))**2-c0))
print('Mink solutions check',sp.simplify(sp.diff(-a*sp.tanh(a*t),t)-(a*sp.tanh(a*t))**2+c0), sp.simplify(0-a**2+c0))
# Random-number check of the K-C-S identity E_k d_delta h^k = 0
import random
rnd=lambda: sp.Rational(random.randint(-9,9),random.randint(1,5))
Jm=sp.zeros(6,6)
for i in range(6):
    for j in range(i+1,6):
        Jm[i,j]=rnd(); Jm[j,i]=-Jm[i,j]
dh=sp.Matrix(3,6,lambda i,j: rnd())   # d_alpha h^k
Jp=dh*Jm*dh.T
V=[sum(sp.LeviCivita(a_,b_,c_)*Jp[b_,c_]*dh[a_,k] for a_ in range(3) for b_ in range(3) for c_ in range(3)) for k in range(6)]
E=[2*sum(Jm[k,l]*V[l] for l in range(6)) for k in range(6)]
print('E_k d_alpha h^k =',[sum(E[k]*dh[al,k] for k in range(6)) for al in range(3)])
# Model C near Sigma: size of the curvature part at c=0.1, Theta=pi/2
r,c=sp.symbols('r c',positive=True)
Dc=r**2-4*c**2*(1+r**2)*(r**2+1)
num=14*c**2*r**8-2*c**2*r**8+14*c**2*r**6+28*c**2*r**6-8*c**2*r**6+34*c**2*r**4-4*c**2*r**4+4*c**2*r**2+2*c**2*r**2-2*c**2-3*r**6-3*r**4
for rr in sp.nroots(Dc.subs(c,sp.Rational(1,10)).as_poly(r)):
    if rr.is_real and rr>0: print('C r_Sigma',rr,'numerator of G^PsiPsi',num.subs({c:sp.Rational(1,10),r:rr}).evalf(6))
