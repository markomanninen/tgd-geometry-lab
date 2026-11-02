# Parallel tori, eikonal, curvatures, moduli, cross-term presentation. E^3 cylindrical (rho,phi,z).
import sympy as sp
R,f=sp.symbols('R f',positive=True); th,ph=sp.symbols('theta phi',real=True)
rho,z=sp.symbols('rho z',positive=True)
F=sp.sqrt((rho-R)**2+z**2)
print("|grad f|^2 =",sp.simplify(sp.diff(F,rho)**2+sp.diff(F,z)**2))
# embedded chart (f,theta,phi): metric df^2 + f^2 dth^2 + (R+f cos th)^2 dphi^2
r=R+f*sp.cos(th)
print("Laplacian f = kappa1+kappa2 =",sp.simplify(1/f+sp.cos(th)/r))
print("kappa1-kappa2 =",sp.simplify(1/f-sp.cos(th)/r))
# Flatness check of ds^2=df^2+f^2 dth^2+r^2 dphi^2 by explicit embedding
X=sp.Matrix([r*sp.cos(ph),r*sp.sin(ph),f*sp.sin(th)])
J=X.jacobian([f,th,ph]); print("embedding metric =",sp.simplify(J.T*J))
# isothermal leaf coordinate thetat with d thetat = f dth / r
P=2*sp.pi*f/sp.sqrt(R**2-f**2)
print("period of thetat P(f) =",P,"  dP/df =",sp.simplify(sp.diff(P,f)))
print("modulus 2pi/P =",sp.simplify(2*sp.pi/P))
tt=2*f/sp.sqrt(R**2-f**2)*sp.atan(sp.sqrt((R-f)/(R+f))*sp.tan(th/2))
print("d thetat/d theta - f/r =",sp.simplify(sp.diff(tt,th)-f/r))
ttf=sp.simplify(sp.diff(tt,f))
print("thetat_f at num point R=2,f=1,th=1:",sp.N(ttf.subs({R:2,f:1,th:1})))
# presentation B metric in (u,v,phi,thetat), f=(v-u)/2, b=thetat_f, rhoT=r: ds2=du dv - r^2(dphi^2+(dtt-b df)^2)
b,rr=sp.symbols('b r',real=True)
g=sp.zeros(4,4); g[0,1]=g[1,0]=sp.Rational(1,2)
# df=(dv-du)/2
E=sp.Matrix([[0,0,1,0],[b/2,-b/2,0,1]])
G=g-rr**2*(E.T*E)
Gi=sp.simplify(G.inv())
print("lower g_uu,g_vv,g_uv =",sp.factor(G[0,0]),sp.factor(G[1,1]),sp.factor(G[0,1]))
print("upper g^uu,g^vv,g^uv =",Gi[0,0],Gi[1,1],Gi[0,1])
print("upper g^{u tt},g^{v tt} =",sp.factor(Gi[0,3]),sp.factor(Gi[1,3]))
print("(grad w)^2 for w=phi+i tt: g^{pp}-g^{tt}+2i g^{pt} =",sp.factor(Gi[2,2]-Gi[3,3]+2*sp.I*Gi[2,3]))
# integrability of M^2
print("Toroidal: |grad tau|=(cosh tau-cos sigma)/a depends on sigma; R=a coth tau, r=a/sinh tau, modulus:")
a,t=sp.symbols('a tau',positive=True)
print(sp.simplify(sp.sqrt((a*sp.coth(t))**2-(a/sp.sinh(t))**2)/(a/sp.sinh(t))))
# Translation family X=X0(w)+u l+v n, torus axis z, l=(1,0,0,1), n=(1,0,0,-1), chart (u,v,phi,tt)
pass
