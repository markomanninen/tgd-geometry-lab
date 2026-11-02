# Check section 2.4. (a) translated torus metric, (b) Riccati/arc-length relation for a null velocity on a hyperbolic circle.
import sympy as sp, numpy as np
print("=== translated torus, chart (u,v,phi,tt); p=rho cos(th)/2")
rho,c=sp.symbols('rho c',positive=True)
p=rho*c/2
G=sp.Matrix([[0,sp.Rational(1,2),0,p],[sp.Rational(1,2),0,0,-p],[0,0,-rho**2,0],[p,-p,0,-rho**2]])
print("det g =",sp.factor(G.det()),"   (with c=cos th, expect -rho^4 (1-c^2)/4)")
Gi=sp.simplify(G.inv()); print("g^uu =",sp.factor(Gi[0,0]),"g^vv =",sp.factor(Gi[1,1]),"(expect -c^2/(1-c^2))")
print("=== hyperbolic circle in half plane (rho,Z), static T=0; AdS3 metric (dT^2-dZ^2-drho^2)/rho^2")
R,a0=2.0,1.0
L=2*np.pi*a0/np.sqrt(R**2-a0**2); d=np.arcsinh(L/(2*np.pi)); k=1/np.tanh(d)
print("length",L,"hyperbolic radius",d,"k=coth d",k)
N=20000; s=np.arange(N)*L/N          # hyperbolic arc length
# circle param: integrate d(alpha)/ds = rho/a0
al=np.zeros(N+1); al[0]=0.0
for i in range(N):
    h=L/N
    f=lambda x:(R+a0*np.cos(x))/a0
    k1=f(al[i]);k2=f(al[i]+h*k1/2);k3=f(al[i]+h*k2/2);k4=f(al[i]+h*k3)
    al[i+1]=al[i]+h*(k1+2*k2+2*k3+k4)/6
print("alpha closure-2pi",al[-1]-2*np.pi)
al=al[:-1]
rho=R+a0*np.cos(al); Z=a0*np.sin(al)
Tv=np.stack([-np.sin(al),np.cos(al)],1)  # euclid unit tangent (rho,Z)
Nv=np.stack([np.cos(al),np.sin(al)],1)   # outward normal in half plane
# hyperbolic outward normal: check it is outward wrt hyperbolic centre: rho direction scaled, sign same
g=0.4*np.sin(2*np.pi*s/L)                 # zero mean choice for ln r via odd function
r=np.exp(g)
print("oint (r-1/r) ds =",np.sum(r-1/r)*L/N)
lnpsi=np.cumsum(k/2*(1/r-r))*L/N
lnpsi-=lnpsi.mean(); print("periodic ln psi jump",(k/2*(1/r-r)).sum()*L/N)
psi=np.exp(lnpsi); A=psi*r/np.sqrt(2); B=psi/(np.sqrt(2)*r)
# velocity in AdS orthonormal frame (e_tau, nu, T): V=psi T + a l + b n, l=(e+nu)/sqrt2, n=(e-nu)/sqrt2
Vt=(A+B)/np.sqrt(2); Vn=(A-B)/np.sqrt(2)
print("null check max|psi^2+Vn^2-Vt^2| =",abs(psi**2+Vn**2-Vt**2).max())
# coordinate velocity: multiply by rho
dT=rho*Vt; dR=rho*(Vn*Nv[:,0]+psi*Tv[:,0]); dZ=rho*(Vn*Nv[:,1]+psi*Tv[:,1])
def seg(eps):
    t=eps*dT; x=rho+eps*dR; z=Z+eps*dZ
    # central differences, periodic, metric at point
    D=lambda q:(np.roll(q,-1)-np.roll(q,1))/(2*L/N)
    return (D(x)**2+D(z)**2-D(t)**2)/x**2
e=1e-4
print("max |d(arc element^2)/ds| =",abs((seg(e)-seg(-e))/(2*e)).max(),"  (zero means arc length preserved)")
print("sanity: flipping the sign of k in psi gives",end=" ")
lp=np.cumsum(-k/2*(1/r-r))*L/N; lp-=lp.mean(); ps=np.exp(lp); A2=ps*r/np.sqrt(2);B2=ps/(np.sqrt(2)*r)
Vt=(A2+B2)/np.sqrt(2);Vn=(A2-B2)/np.sqrt(2)
dT=rho*Vt; dR=rho*(Vn*Nv[:,0]+ps*Tv[:,0]); dZ=rho*(Vn*Nv[:,1]+ps*Tv[:,1])
print(abs((seg(e)-seg(-e))/(2*e)).max())
