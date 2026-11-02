# Metric algebra for the H-J question. Signature (+,-,-,-).
import sympy as sp
print("=== 1. Line element (2.4.19) with lower g_++ = g_-- = 0: upper components")
A,C=sp.symbols('A C',real=True)
B,Bb,D,Db=sp.symbols('B Bb D Db')
# coordinates order (S+,S-,w,wb); ds2 = A dS+dS- + C dw dwb + B dS+dw + Bb dS+dwb + D dS-dw + Db dS-dwb
g=sp.Matrix([[0,A/2,B/2,Bb/2],[A/2,0,D/2,Db/2],[B/2,D/2,0,C/2],[Bb/2,Db/2,C/2,0]])
det=sp.factor(g.det()); adj=g.adjugate()
print("det g =",det)
print("g^{++} det g =",sp.factor(adj[0,0]))
print("g^{--} det g =",sp.factor(adj[1,1]))
print("g^{+-} det g =",sp.factor(adj[0,1]))
print("=== 2. Double null form with shifts: g^{uu}=g^{vv}=0 for any shift")
a,h11,h12,h22,p1,p2,q1,q2=sp.symbols('a h11 h12 h22 p1 p2 q1 q2')
# ds2 = (2/a) du dv - h_ij (dy^i+p^i du+q^i dv)(dy^j+p^j du+q^j dv)
h=sp.Matrix([[h11,h12],[h12,h22]]); P=sp.Matrix([p1,p2]); Q=sp.Matrix([q1,q2])
E=sp.Matrix([[P[0],Q[0],1,0],[P[1],Q[1],0,1]])   # rows: dy^i+... in basis du,dv,dy1,dy2
G=-(E.T*h*E)
G[0,1]+=1/a; G[1,0]+=1/a
Gi=sp.simplify(G.inv())
print("g^{uu},g^{vv},g^{uv} =",Gi[0,0],Gi[1,1],sp.simplify(Gi[0,1]))
print("lower g_uu =",sp.factor(G[0,0])," g_vv =",sp.factor(G[1,1]))
print("=== 3. Weierstrass (3.3): block inverse")
guv,guwb,gvw,gwwb=sp.symbols('g_uv g_uwb g_vw g_wwb')
W=sp.Matrix([[0,guv,0,guwb],[guv,0,gvw,0],[0,gvw,0,gwwb],[guwb,0,gwwb,0]])
Wi=sp.simplify(W.inv()); print(Wi); print("det =",sp.factor(W.det()))
print("=== 4. Real surface xi(u,w), induced metric on X^4 in M^4 x (2-dim fibre)")
s,xu,xw=sp.symbols('s xi_u xi_w'); xub,xwb=sp.symbols('xib_u xib_w')
# ds2 = du dv - dw dwb - s (xu du + xw dw)(xub du + xwb dwb)
R=sp.Matrix([[-s*xu*xub,sp.Rational(1,2),-s*xub*xw/2,-s*xu*xwb/2],
             [sp.Rational(1,2),0,0,0],
             [-s*xub*xw/2,0,0,-sp.Rational(1,2)-s*xw*xwb/2],
             [-s*xu*xwb/2,0,-sp.Rational(1,2)-s*xw*xwb/2,0]])
Ri=sp.simplify(R.inv())
print("g^{uu},g^{uw},g^{uwb},g^{ww} =",Ri[0,0],Ri[0,2],Ri[0,3],Ri[2,2])
print("g^{vv} =",sp.factor(Ri[1,1]))
print("g^{vw} =",sp.factor(Ri[1,2]))
