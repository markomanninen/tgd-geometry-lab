#!/usr/bin/env python3
"""Clifford torus versus holomorphic roots. Fubini-Study with CP1 area pi R^2, R=1."""
import numpy as np, itertools
rng=np.random.default_rng(1)
def h(xi):
    x1,x2=xi; D=1+abs(x1)**2+abs(x2)**2
    return np.array([[ (D-abs(x1)**2)/D**2, -np.conj(x1)*x2/D**2],
                     [ -np.conj(x2)*x1/D**2, (D-abs(x2)**2)/D**2]])
def g(X,Y,xi): return np.real(X@h(xi)@np.conj(Y))
def J(X,Y,xi): return -np.imag(X@h(xi)@np.conj(Y))   # g(iX,Y) up to the overall sign
def area_density(xi,X,Y):
    return np.sqrt(g(X,X,xi)*g(Y,Y,xi)-g(X,Y,xi)**2)
def TT(a,b):
    t1,t2=rng.uniform(0,2*np.pi,2); xi=np.array([a*np.exp(1j*t1),b*np.exp(1j*t2)])
    X=np.array([1j*xi[0],0]); Y=np.array([0,1j*xi[1]])
    return xi,X,Y
xi,X,Y=TT(1,1)
print("# (a) Kahler form and area on T(a,b)={|x1|=a,|x2|=b}")
print("J(X,Y) at a=b=1:",J(X,Y,xi)," at a=.7,b=1.3:",(lambda q:J(q[1],q[2],q[0]))(TT(.7,1.3)))
A=lambda a,b:(4*np.pi**2)*(lambda q:area_density(q[0],q[1],q[2]))(TT(a,b))
print("Area T(1,1)=",A(1,1)," 4pi^2/(3 sqrt3)=",4*np.pi**2/(3*np.sqrt(3))," area/pi=",A(1,1)/np.pi)
print("Area near (1,1):",[round(A(1+d,1-e),5) for d,e in ((.05,0),(-.05,0),(0,.05),(.05,.05),(.05,-.05))])
print("\n# (b) Rank of monomial evaluation matrix: a nonzero holomorphic polynomial vanishes on the set iff rank<number of monomials")
def monos(D): return [(m,n) for m in range(D+1) for n in range(D+1-m)]
def rank_on(pts,D):
    M=monos(D); E=np.array([[p[0]**m*p[1]**n for m,n in M] for p in pts])
    E=E/np.maximum(np.abs(E).max(axis=0,keepdims=True),1e-300)
    return len(M),np.linalg.matrix_rank(E,tol=1e-9)
N=600
th=rng.uniform(0,2*np.pi,(N,2))
tor=np.exp(1j*th)
rp=rng.normal(size=(N,2))                 # RP2 affine chart, real points
line=np.c_[(a:=rng.normal(size=N)+1j*rng.normal(size=N)),(1+2*a)]          # complex line x2=1+2x1
# smooth cubic x2^2=x1^3-x1+1 (genus 1 torus, d=3)
z=rng.normal(size=N)+1j*rng.normal(size=N); cub=np.c_[z,np.sqrt(z**3-z+1)]
for D in (1,3,6):
    print(f"D={D}: Clifford torus {rank_on(tor,D)}, RP2 {rank_on(rp,D)}, line {rank_on(line,D)}, cubic {rank_on(cub,D)}")
print("\n# (c) Fourier form: P on |x1|=|x2|=1 is sum a_mn e^{i(m t1+n t2)}, so P=0 on the torus forces all a_mn=0.")
c=rng.normal(size=(5,5))+1j*rng.normal(size=(5,5))
t=2*np.pi*np.arange(16)/16
vals=np.array([[sum(c[m,n]*np.exp(1j*(m*a+n*b)) for m in range(5) for n in range(5)) for b in t] for a in t])
print("FFT recovers a_mn, max error:",np.abs(np.fft.fft2(vals)[:5,:5]/256-c).max())
print("\n# (d) Tangent plane test: J-invariant plane has |J(e1,e2)|=1, Lagrangian has 0")
def kahler_cos(xi,X,Y):
    return abs(J(X,Y,xi))/area_density(xi,X,Y)
print("torus:",kahler_cos(*TT(1,1)))
x1=.3+.4j; x2=1+2*x1; Xc=np.array([1,2]); Yc=1j*Xc
print("line x2=1+2x1:",kahler_cos(np.array([x1,x2]),Xc,Yc))
print("\n# (e) table consequence, S=area/(pi R^2)")
print("Lagrangian Clifford 8GT=",A(1,1)/np.pi,"Lambda R^2; RP2 (area 2 pi R^2): 2 Lambda R^2; S^2 double cover: 4 Lambda R^2")
