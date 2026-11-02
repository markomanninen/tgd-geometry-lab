# Numeric and symbolic checks of examples. Signature (+,-,-,-).
import sympy as sp, numpy as np
t,x,y,z=sp.symbols('t x y z',real=True); X=[t,x,y,z]; eta=[1,-1,-1,-1]
def up(f): return [eta[i]*sp.diff(f,X[i]) for i in range(4)]
def dot(f,g): return sum(eta[i]*sp.diff(f,X[i])*sp.diff(g,X[i]) for i in range(4))
def comm(a,b): return [sum(a[j]*sp.diff(b[i],X[j])-b[j]*sp.diff(a[i],X[j]) for j in range(4)) for i in range(4)]
def m2_integrable(u,v,pts):
    l,n=up(u),up(v); c=comm(l,n)
    fn=sp.lambdify(X,[dot(u,u),dot(v,v),dot(u,v)]+l+n+c,'numpy')
    res=[]
    for p in pts:
        o=np.array(fn(*p),dtype=float)
        M=np.array([o[3:7],o[7:11],o[11:15]])
        sv=np.linalg.svd(M,compute_uv=False)
        res.append((o[0],o[1],o[2],sv[2]/sv[0]))
    return res
rho=sp.sqrt(x**2+y**2)
pts=[(0.3,1.2,0.4,0.2),(0.1,0.9,-0.3,0.5),(0.2,1.5,0.5,-0.4)]
print("=== parallel tori u=t-f,v=t+f (uu,vv,uv,smallest sv of l,n,[l,n])")
f=sp.sqrt((rho-1)**2+z**2)
for r in m2_integrable(t-f,t+f,pts): print(r)
print("=== two cones, vertices on z axis at +-d, u=t-|x-a|,v=t+|x-b|")
d=sp.Rational(1,2)
r1=sp.sqrt(x**2+y**2+(z-d)**2); r2=sp.sqrt(x**2+y**2+(z+d)**2)
for r in m2_integrable(t-r1,t+r2,pts): print(r)
print("=== two circles R1=1,R2=1.4, u=t-f1,v=t+f2 (elliptic torus)")
f1=sp.sqrt((rho-1)**2+z**2); f2=sp.sqrt((rho-sp.Rational(7,5))**2+z**2)
for r in m2_integrable(t-f1,t+f2,pts): print(r)
print("=== leaf of two-cone family lies in a hyperplane: difference of quadrics")
T,U,V=sp.symbols('T U V')
q=sp.expand(((T-U)**2-(x**2+y**2+(z-d)**2))-((T-V)**2-(x**2+y**2+(z+d)**2)))
print(q)
# elliptic torus numeric: leaf f1+f2=c parametrised, induced metric spacelike and shear
print("=== elliptic torus leaf: f1+f2=c, foci (1,0),(1.4,0), c=1.0; t=u0+f1")
c=1.0; a0=c/2; e=0.2; b0=np.sqrt(a0**2-e**2); s=np.linspace(0,2*np.pi,721)
rho_=1.2+a0*np.cos(s); z_=b0*np.sin(s); f1_=np.hypot(rho_-1,z_); f2_=np.hypot(rho_-1.4,z_)
print("max|f1+f2-c| =",abs(f1_+f2_-c).max())
ds=np.gradient(s); tt=np.gradient(f1_,s); rr=np.gradient(rho_,s); zz=np.gradient(z_,s)
print("min of rho_s^2+z_s^2-t_s^2 (positive means spacelike) =",(rr**2+zz**2-tt**2).min())
print("modulus 2pi/P: P=int sqrt(...)/rho =",np.trapezoid(np.sqrt(rr**2+zz**2-tt**2)/rho_,s))

print("=== Robinson congruence on toroidal tori, t=0, a=1")
a=1
D=x**2+y**2+z**2+a**2
n=[2*(x*z+a*y)/D, 2*(y*z-a*x)/D, (z**2+a**2-x**2-y**2)/D]
print("n.n-1 =",sp.simplify(sum(c**2 for c in n)-1))
d1=sp.sqrt((sp.sqrt(x**2+y**2)+a)**2+z**2); d2=sp.sqrt((sp.sqrt(x**2+y**2)-a)**2+z**2)
tau=sp.log(d1/d2)
E3=[x,y,z]
print("n.grad tau =",sp.simplify(sum(n[i]*sp.diff(tau,E3[i]) for i in range(3))))
curl=[sp.diff(n[2],y)-sp.diff(n[1],z),sp.diff(n[0],z)-sp.diff(n[2],x),sp.diff(n[1],x)-sp.diff(n[0],y)]
tw=sp.simplify(sum(n[i]*curl[i] for i in range(3))); print("twist n.curl n =",tw)
Jn=sp.lambdify((x,y,z),sp.Matrix(3,3,lambda i,j:sp.diff(n[j],E3[i])),'numpy')
nf=sp.lambdify((x,y,z),n,'numpy')
for p in [(0.3,0.7,-0.2),(1.1,-0.4,0.6)]:
    N=np.array(nf(*p),float); J=np.array(Jn(*p),float)
    e1=np.cross(N,[1,0,0]); e1/=np.linalg.norm(e1); e2=np.cross(N,e1)
    S=np.array([[e@J@g for g in (e1,e2)] for e in (e1,e2)])
    sym=(S+S.T)/2; tf=sym-np.trace(sym)/2*np.eye(2)
    print(" shear norm =",np.linalg.norm(tf)," expansion =",np.trace(S)," rot =",(S[0,1]-S[1,0])/2)
print("=== shear of u=t-f parallel torus: (k1-k2)/2 =R/(2 f (R+f cos th)) nonzero, see m2")

print("=== criterion: J=grad V x grad |grad V|^2 vanishes iff |grad V| function of V")
r=sp.sqrt(x**2+y**2+z**2)
def crit(V,pt):
    g=[sp.diff(V,c) for c in E3]; N=sum(c**2 for c in g); h=[sp.diff(N,c) for c in E3]
    cr=[g[1]*h[2]-g[2]*h[1],g[2]*h[0]-g[0]*h[2],g[0]*h[1]-g[1]*h[0]]
    lap=sum(sp.diff(V,c,2) for c in E3)
    f=sp.lambdify(E3,cr+[lap],'numpy'); o=np.array(f(*pt),float)
    return np.linalg.norm(o[:3]),o[3]
p=(0.7,0.4,0.9)
d=0.5
cases={"plane x":x,"monopole 1/r":1/r,"line log rho":sp.log(rho),
 "point dipole z/r^3":z/r**3,"quadrupole (3z^2-r^2)/r^5":(3*z**2-r**2)/r**5,
 "two charges +-":1/sp.sqrt(x**2+y**2+(z-d)**2)-1/sp.sqrt(x**2+y**2+(z+d)**2),
 "two dipoles x/r^3 + z/r^3":(x+z)/r**3,
 "Stokes dipole rho^2/r^3":rho**2/r**3,
 "parallel torus f":sp.sqrt((rho-1)**2+z**2)}
for k,V in cases.items(): print(f"{k:32s} |J|={crit(V,p)[0]:.6g}  Laplacian={crit(V,p)[1]:.6g}")
print("=== antiperiodic S^2 potential: log tan(th/2) Legendre coefficients")
from numpy.polynomial import legendre as L
xs,ws=L.leggauss(4000)
g=0.5*np.log((1-xs)/(1+xs))
for l in range(0,7):
    P=L.legval(xs,[0]*l+[1]); cf=(2*l+1)/2*np.sum(ws*g*P)
    print(l,round(cf,5), "pred", round(-(2*l+1)/(l*(l+1)),5) if l%2 and l>0 else 0)
