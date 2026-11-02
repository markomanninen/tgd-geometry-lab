# Boundary terms at a signature-changing light-like surface. Signature (+,-,-,-).
# Convention: R^r_{s m n} = d_m G^r_{n s} - ..., R_{sn} = R^r_{s r n}, R = g^{sn} R_{sn}.
import sympy as sp, mpmath as mp

def curv(g, X):
    n=len(X); gi=g.inv().applyfunc(sp.simplify)
    G=[[[sum(gi[r,l]*(sp.diff(g[l,m],X[k])+sp.diff(g[l,k],X[m])-sp.diff(g[m,k],X[l])) for l in range(n))/2
         for k in range(n)] for m in range(n)] for r in range(n)]
    def Ric(s,nu):
        e=0
        for r in range(n):
            e+=sp.diff(G[r][nu][s],X[r])-sp.diff(G[r][r][s],X[nu])
            for l in range(n):
                e+=G[r][r][l]*G[l][nu][s]-G[r][nu][l]*G[l][r][s]
        return e
    Rc=sp.Matrix(n,n,lambda i,j: Ric(i,j))
    R=sp.simplify(sum(gi[i,j]*Rc[i,j] for i in range(n) for j in range(n)))
    return R,Rc.applyfunc(sp.simplify),gi

t,x,y,z=sp.symbols('t x y z',real=True)
print("=== A. Model f=x, both sides")
R,_,_=curv(sp.diag(x,-1,-1,-1),[t,x,y,z])
print("R(f=x) =",R,"  (rational, holds on both sides)")
print("2 N''/N with N=sqrt|x|, x>0:",sp.simplify(2*sp.diff(sp.sqrt(x),x,2)/sp.sqrt(x)))
e,L=sp.symbols('epsilon L',positive=True); s=sp.Symbol('s',positive=True)
def B(N,arg): return 2*sp.diff(N,s).subs(s,arg)      # 2 d_s sqrt|h| at distance arg
right=sp.integrate(sp.simplify(-sp.Rational(1,2)*s**sp.Rational(-3,2)),(s,e,L))
left =right                                            # sqrt|g|R is even in x
print("int_eps^L sqrt|g|R =",right,"; int_-L^-eps =",left)
print("GHY-type term with outward normal, -2 n_out(sqrt|h|), at +eps =",B(sp.sqrt(s),e),
      "; at -eps (mirror, same sign) =",B(sp.sqrt(s),e))
print("sum bulk+GHY right side =",sp.simplify(right+B(sp.sqrt(s),e)))
print("analytic sqrt(g): left side multiplied by +-i, divergent parts -1/sqrt(eps)(1 +- i), no cancellation between sides")
print("det g_4 = -x, det g_3 on x=0 with coordinates (t,y,z) =",sp.Matrix.diag(0,-1,-1).det()," kernel = d_t (tangent)")
print("g^{xx} =",-1," (normal covector dx has norm -1, stays spacelike)")
# distribution check: 2 d^2 sqrt|x| paired with test function equals Hadamard finite part, no delta
mp.mp.dps=25
phi=lambda u: mp.e**(-u*u); phi2=lambda u:(4*u*u-2)*mp.e**(-u*u)
lhs=2*mp.quad(lambda u:2*mp.sqrt(u)*phi2(u),[0,1,8])
eps=mp.mpf('1e-7')
fp =2*(mp.quad(lambda u:-0.5*u**(-1.5)*phi(u),[eps,1e-3,1,8]))+2/mp.sqrt(eps)
print("pairing with exp(-x^2): distribution",lhs," finite part (eps=1e-7)",fp)

print("\n=== B. Exact embedding, X^4 -> M^4 x S^2(r): theta=n/r, phi=w t")
r,w=sp.symbols('r omega',positive=True); th=sp.Symbol('theta',real=True)
Hm=sp.diag(1,-1,-1,-1,-r**2,-r**2*sp.sin(th)**2)        # (T,X,Y,Z,theta,phi)
emb=sp.Matrix([t,0,y,z,th,w*t]); Xc=[t,th,y,z]
Jac=emb.jacobian(Xc); g=(Jac.T*Hm*Jac).applyfunc(sp.simplify); print("induced g =",g)
A=g[0,0]; th0=sp.asin(1/(w*r))
print("g_tt(theta0) =",sp.simplify(A.subs(th,th0)),"  d g_tt/d theta at theta0 =",sp.simplify(sp.diff(A,th).subs(th,th0)))
print("lift of kernel e=(1,0,0,0,0,omega) has h(e,e) at theta0 =",sp.simplify(1-w**2*r**2*sp.sin(th0)**2))
print("Normal acceleration check -2 h(d_th, nabla_e e) =",-2*(-r**2)*(-w**2*sp.sin(th)*sp.cos(th)),"vs d_th g_tt =",sp.diff(A,th))
print("equator theta0=pi/2, w r=1: g_tt =",sp.simplify(A.subs(w,1/r)),"(double zero, no sign change)")
Rm,_,_=curv(g,Xc); print("R (helicoid x R^2) =",sp.simplify(Rm))
# volume field equation for phi(t,theta): only derivatives of phi enter
pt,pth=sp.symbols('p_t p_th',real=True); S2=r**2*sp.sin(th)**2
gtt=1-S2*pt**2; gtth=-S2*pt*pth; gthth=-r**2-S2*pth**2; D=gtt*gthth-gtth**2
Lg=sp.sqrt(-D); print("d L/d phi_th at phi_th=0 =",sp.simplify(sp.diff(Lg,pth).subs(pth,0)),
  " d L/d phi_t independent of t, so E-L phi-equation holds at phi=omega t")

print("\n=== C. Non-static a=1 model h_tt=x a(t,y), c(t,x)=c0(t)+c1(t) x")
a=sp.Function('a')(t,y); c0f=sp.Function('c0')(t); c1f=sp.Function('c1')(t)
xp=sp.Symbol('x',positive=True); cc=c0f+c1f*xp
gg=sp.diag(xp*a,-1,-cc**2,-cc**2)
Rg,_,_=curv(gg,[t,xp,y,z])
x2R=sp.limit(sp.simplify(xp**2*Rg),xp,0); print("lim x^2 R =",x2R)
sh=sp.sqrt(a)*sp.sqrt(xp)*cc**2
Rem=sp.simplify(sh*Rg-2*sp.diff(sh,xp,2))
c1R=sp.simplify(sp.limit(sp.simplify(Rem*sp.sqrt(xp)),xp,0))
print("x^{1/2}(sqrt|g|R - 2 d_x^2 sqrt|h|) at 0 =",c1R,"  (finite: remainder is integrable)")
print("pi^y_y = sqrt|h|(K^y_y-K) ~",sp.simplify(sp.limit(sp.sqrt(xp)*sh*(sp.diff(sp.log(cc),xp)-(1/(2*xp)+2*sp.diff(sp.log(cc),xp))),xp,0)),"/sqrt(x)")
print("pi^t_t = sqrt|h|(K^t_t-K) at 0 =",sp.simplify(sp.limit(sh*(-2*sp.diff(sp.log(cc),xp)),xp,0)))

print("\n=== D. Power family N=|n|^(a/2): sqrt|g|R=2N'', boundary term 2N'")
pa=sp.Symbol('a',positive=True); n=sp.Symbol('n',positive=True)
N=n**(pa/2); print("2N'' =",sp.simplify(2*sp.diff(N,n,2)),"; 2N' =",sp.simplify(2*sp.diff(N,n)))
for av in [1,2,3]:
    print(" a=%d: 2N'(eps)="%av,sp.simplify(2*sp.diff(N,n).subs(pa,av)),"  g^tt sqrt|g| =",n**(-sp.Rational(av,2)))
print("a=2: d^2|n| = 2 delta(n), so sqrt|g|R = 2(k_+ + k_-) delta(n) for N=k_+- |n|")

print("\n=== E. a=3 from g=eta-df df with f=t(1+x^3/2) in (t,x)")
f=t*(1+x**3/2)
g2=sp.Matrix([[1-sp.diff(f,t)**2,-sp.diff(f,t)*sp.diff(f,x)],[-sp.diff(f,t)*sp.diff(f,x),-1-sp.diff(f,x)**2]])
Dd=sp.factor(sp.simplify(g2.det())); print("det block =",Dd,"  series:",sp.series(Dd,x,0,5))
print("on x=0: A,B,C =",[sp.simplify(q.subs(x,0)) for q in (g2[0,0],g2[0,1],g2[1,1])])
g4=sp.diag(g2,-1,-1)
R3,_,_=curv(g4,[t,x,y,z]); print("x^2 R at x->0 =",sp.limit(sp.simplify(x**2*R3),x,0))

print("\n=== F. True null limit, Rindler chart of dU dV - q(U,V)^2 (dy^2+dz^2)")
U,V=sp.symbols('U V',real=True); q=1+U*V**2+V        # any regular example
n,T=sp.symbols('n T',positive=True)                  # V=e^{+T} fixed on future horizon
tt=sp.Symbol('tt',real=True)
qc=q.subs({U:-n*sp.exp(-tt),V:n*sp.exp(tt)},simultaneous=True)
Bf=2*sp.diff(n*qc**2,n)
Bfh=sp.limit(Bf.subs(tt,sp.log(V/n)).subs(V,T),n,0)
qh=q.subs({U:0,V:T}); theta=T*sp.diff(sp.log(qh**2),T)
print("limit of 2 d_n(n q^2) on U=0 =",sp.simplify(Bfh)," vs 2 q^2 (kappa+Theta) =",sp.simplify(2*qh**2*(1+theta)),
      " difference",sp.simplify(Bfh-2*qh**2*(1+theta)))

print("\n=== G. Warped model ds^2=N^2dt^2-drho^2-r^2 dphi^2-dz^2 (M^1 x X^2 x S^1 when N=1)")
rho=sp.Symbol('rho',positive=True); Nf=sp.Function('N')(rho); rf=sp.Function('r')(rho); ph=sp.Symbol('phi',real=True)
gw=sp.diag(Nf**2,-1,-rf**2,-1); Rw,Rcw,giw=curv(gw,[t,rho,ph,z])
RX=-2*sp.diff(rf,rho,2)/rf
chk=sp.simplify(Nf*rf*Rw-(-Nf*rf*RX+2*sp.diff(rf*sp.diff(Nf,rho),rho)))
print("sqrt|g|R + N r R_X - 2 (r N')' =",chk)
Gtt=sp.simplify(giw[0,0]*Rcw[0,0]-Rw/2); print("G^t_t - (-(1/2)... ) : G^t_t =",Gtt," ; G^t_t + R_X/2 =",sp.simplify(Gtt+RX/2),"or",sp.simplify(Gtt-RX/2))
print("GHY at outer rho0 is -2 d_rho(N r)=-2 N' r -2 N r'; N->0 keeps only -2 N' r.")
def S(Nfun,rho0,chi_check=True):
    return 2*mp.pi*mp.quad(lambda q:2*mp.sin(q)*Nfun(q),[0,rho0])
print("Unit sphere cap rho<rho0, value of int N R_X dA + 2 N(rho0) oint k_g, target 4 pi chi = 4 pi =",4*mp.pi)
for rho0 in [0.5,1.0,1.4,1.5,mp.pi/2]:
    w0=1/mp.sin(rho0)
    Nh=lambda q:mp.sqrt(max(mp.mpf(0),1-(w0*mp.sin(q))**2))
    N1=lambda q:mp.mpf(1)
    prod=S(N1,rho0)+2*2*mp.pi*mp.cos(rho0)
    orb =S(Nh,rho0)
    print("  rho0=%.3f  N=1: %.6f   N^2=1-sin^2/sin^2rho0: %.6f   ratio to 4pi %.4f"%(rho0,prod,orb,orb/(4*mp.pi)))
print("Second lapse with the same zero, N^2=1-rho/rho0:")
for rho0 in [1.0,1.5]:
    Nl=lambda q:mp.sqrt(max(mp.mpf(0),1-q/rho0)); o=S(Nl,rho0); print("  rho0=%.3f  %.6f ratio %.4f"%(rho0,o,o/(4*mp.pi)))
print("n=2 annulus: both boundaries have N->0. N=1 gives 4 pi chi = 0.")
for r1 in [0.3,0.7,1.2]:
    Nz=lambda q:mp.sqrt(max(mp.mpf(0),1-(mp.sin(r1)/mp.sin(q))**2))
    o=2*mp.pi*mp.quad(lambda q:2*mp.sin(q)*Nz(q),[r1,mp.pi/2,mp.pi-r1])
    print("  sphere band rho1=%.2f  int N R_X dA = %.6f"%(r1,o))
for r1 in [1.0,3.0,6.0]:
    Nc=lambda q:mp.sqrt(max(mp.mpf(0),1-(q/r1)**2))
    Kc=lambda q:-2/mp.cosh(q)**4
    o=2*mp.pi*mp.quad(lambda q:Kc(q)*mp.cosh(q)**2*Nc(q),[-r1,0,r1])
    b=2*mp.pi*mp.quad(lambda q:Kc(q)*mp.cosh(q)**2,[-r1,0,r1])
    print("  catenoid rho1=%.1f  int N R_X dA = %.6f  (N=1 interior %.6f, N=1 with 2 oint k_g = 0)"%(r1,o,b))

print("\n=== H. Boundary variation, metric N^2dt^2-dn^2-c(n)^2(dy^2+dz^2)")
m=sp.Symbol('n',positive=True); Nn=sp.Function('N')(m); cn=sp.Function('c')(m)
Rh,_,_=curv(sp.diag(Nn**2,-1,-cn**2,-cn**2),[t,m,y,z])
L1=-2*(2*sp.diff(Nn,m)*cn*sp.diff(cn,m)+Nn*sp.diff(cn,m)**2)
print("sqrt|g|R - 2 (N c^2)'' - L1 =",sp.simplify(Nn*cn**2*Rh-2*sp.diff(Nn*cn**2,m,2)-L1))
al=sp.Symbol('alpha',positive=True); cs=sp.Symbol('c',positive=True); cp=sp.Symbol('cp',real=True)
print("dL1/dc' with N=sqrt(alpha n), leading x sqrt(n):",sp.limit(sp.sqrt(m)*(-4*sp.diff(sp.sqrt(al*m),m)*cs-4*sp.sqrt(al*m)*cp),m,0))
print("So at n=eps: S_1 var = +sqrt(alpha)/sqrt(eps) d(c^2); B=sqrt(alpha)c^2/sqrt(eps);")
print("S_EH=S_1-B var = -(c^2/sqrt(eps)) d sqrt(alpha); S_EH+GHY=S_1 var = sqrt(alpha)/sqrt(eps) d(c^2).")
print("S_1+(mu-1)B var = [mu sqrt(alpha) d(c^2) + (mu-1) c^2 d sqrt(alpha)]/sqrt(eps): no mu removes both.")
