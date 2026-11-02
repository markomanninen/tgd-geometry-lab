# Truncated Taylor jets in 4 real chart variables, and the field equations of a 4-surface
# in M^4 x CP_2.  M^4 is Cartesian (t,x,y,z), signature (+,-,-,-).  CP_2 uses the affine
# Fubini-Study form with g_H = m - h, as in pallo_u_tarkistus.py.  Everything is evaluated
# at the chart origin, so no simplification of large expressions is needed.
import itertools, mpmath as mp
mp.mp.dps=40
NV=4; N=3
MON=[e for e in itertools.product(range(N+1),repeat=NV) if sum(e)<=N]
MON.sort(key=sum)
IDX={e:i for i,e in enumerate(MON)}
L=len(MON)
TAB=[(i,j,IDX[tuple(a+b for a,b in zip(MON[i],MON[j]))]) for i in range(L) for j in range(L)
     if sum(MON[i])+sum(MON[j])<=N]
Z=mp.mpc(0)
class J:
    __slots__=('c',)
    def __init__(s,c=None): s.c=c if c is not None else [Z]*L
    @staticmethod
    def const(x):
        c=[Z]*L; c[0]=mp.mpc(x); return J(c)
    @staticmethod
    def var(i,x0=0):
        c=[Z]*L; c[0]=mp.mpc(x0); e=[0]*NV; e[i]=1; c[IDX[tuple(e)]]=mp.mpc(1); return J(c)
    def __add__(s,o):
        if not isinstance(o,J): o=J.const(o)
        return J([a+b for a,b in zip(s.c,o.c)])
    __radd__=__add__
    def __neg__(s): return J([-a for a in s.c])
    def __sub__(s,o): return s+(-o if isinstance(o,J) else J.const(-o))
    def __rsub__(s,o): return (-s)+o
    def __mul__(s,o):
        if not isinstance(o,J): return J([a*o for a in s.c])
        r=[Z]*L; a=s.c; b=o.c
        for i,j,k in TAB:
            if a[i]!=0 and b[j]!=0: r[k]=r[k]+a[i]*b[j]
        return J(r)
    __rmul__=__mul__
    def compose(s,co):
        # co[k]: Taylor coefficients of f at s.c[0]
        e=J(list(s.c)); e.c[0]=Z
        r=J.const(co[N]); 
        for k in range(N-1,-1,-1): r=r*e+co[k]
        return r
    def inv(s):
        x=s.c[0]; return s.compose([(-1)**k/x**(k+1) for k in range(N+1)])
    def __truediv__(s,o):
        if not isinstance(o,J): return s*(1/mp.mpc(o))
        return s*o.inv()
    def __rtruediv__(s,o): return s.inv()*o
    def __pow__(s,n):
        r=J.const(1)
        for _ in range(n): r=r*s
        return r
    def sqrt(s):
        x=s.c[0]; rt=mp.sqrt(x); co=[rt*mp.binomial(mp.mpf(1)/2,k)/x**k for k in range(N+1)]
        return s.compose(co)
    def exp(s):
        x=mp.exp(s.c[0]); return s.compose([x/mp.factorial(k) for k in range(N+1)])
    def sin(s):
        sn,cs=mp.sin(s.c[0]),mp.cos(s.c[0]); t=[sn,cs,-sn,-cs]
        return s.compose([t[k%4]/mp.factorial(k) for k in range(N+1)])
    def cos(s):
        sn,cs=mp.sin(s.c[0]),mp.cos(s.c[0]); t=[cs,-sn,-cs,sn]
        return s.compose([t[k%4]/mp.factorial(k) for k in range(N+1)])
    def conj(s): return J([mp.conj(a) for a in s.c])
    def d(s,i):
        r=[Z]*L
        for k,e in enumerate(MON):
            if e[i]>0:
                f=list(e); f[i]-=1; r[IDX[tuple(f)]]=s.c[k]*e[i]
        return J(r)
    def v(s): return s.c[0]

ETA=[1,-1,-1,-1]
def box(f): return sum((f.d(i).d(i)*ETA[i] for i in range(4)),J.const(0)).v()
def dot(f,h): return sum((f.d(i)*h.d(i)*ETA[i] for i in range(4)),J.const(0))

def surface(x,xi,xib=None):
    """x: 4 jets t,x,y,z.  xi: 2 jets.  xib: conjugates, default coefficientwise conj (real chart)."""
    if xib is None: xib=[e.conj() for e in xi]
    n=4
    dx=[[x[m].d(a) for a in range(n)] for m in range(4)]
    dz=[[xi[k].d(a) for a in range(n)] for k in range(2)]
    dzb=[[xib[k].d(a) for a in range(n)] for k in range(2)]
    D=1+xi[0]*xib[0]+xi[1]*xib[1]; Di=D.inv()
    h=[[ (Di if k==l else J.const(0))-xib[k]*xi[l]*Di*Di for l in range(2)] for k in range(2)]
    gj=[[None]*n for _ in range(n)]
    for a in range(n):
        for b in range(a,n):
            e=J.const(0)
            for m in range(4): e=e+dx[m][a]*dx[m][b]*ETA[m]
            for k in range(2):
                for l in range(2):
                    e=e-h[k][l]*(dz[k][a]*dzb[l][b]+dz[k][b]*dzb[l][a])*(mp.mpf(1)/2)
            gj[a][b]=e; gj[b][a]=e
    g=mp.matrix(n,n); dg=[mp.matrix(n,n) for _ in range(n)]; ddg=[[mp.matrix(n,n) for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            g[a,b]=gj[a][b].v()
            for c in range(n):
                t=gj[a][b].d(c); dg[c][a,b]=t.v()
                for e in range(n): ddg[c][e][a,b]=t.d(e).v()
    gi=g**-1
    # lower Christoffels and derivatives
    Gl=[[[ (dg[b][d,c]+dg[c][d,b]-dg[d][b,c])/2 for c in range(n)] for b in range(n)] for d in range(n)]
    dGl=[[[[ (ddg[b][e][d,c]+ddg[c][e][d,b]-ddg[d][e][b,c])/2 for e in range(n)] for c in range(n)] for b in range(n)] for d in range(n)]
    dgi=[gi*0 for _ in range(n)]
    for e in range(n): dgi[e]=-(gi*dg[e]*gi)
    Gam=[[[sum(gi[c,d]*Gl[d][a][b] for d in range(n)) for b in range(n)] for a in range(n)] for c in range(n)]
    dGam=[[[[sum(dgi[e][c,d]*Gl[d][a][b]+gi[c,d]*dGl[d][a][b][e] for d in range(n)) for e in range(n)] for b in range(n)] for a in range(n)] for c in range(n)]
    Ric=mp.matrix(n,n)
    for b in range(n):
        for d in range(n):
            s=0
            for a in range(n):
                s+=dGam[a][b][d][a]-dGam[a][a][d][b]
                for e in range(n):
                    s+=Gam[a][a][e]*Gam[e][b][d]-Gam[a][d][e]*Gam[e][a][b]
            Ric[b,d]=s
    R=sum(gi[a,b]*Ric[a,b] for a in range(n) for b in range(n))
    Gi=gi*(Ric-g*(R/2))*gi
    zb=[xib[0].v(),xib[1].v()]; Dv=D.v()
    B=[]  # 6 components: t,x,y,z,xi1,xi2 (conjugates follow)
    for m in range(4):
        B.append([[dx[m][a].d(b).v()-sum(Gam[c][a][b]*dx[m][c].v() for c in range(n)) for b in range(n)] for a in range(n)])
    for k in range(2):
        Bk=[[None]*n for _ in range(n)]
        for a in range(n):
            for b in range(n):
                pa=sum(zb[j]*dz[j][a].v() for j in range(2)); pb=sum(zb[j]*dz[j][b].v() for j in range(2))
                Bk[a][b]=dz[k][a].d(b).v()-sum(Gam[c][a][b]*dz[k][c].v() for c in range(n))-(dz[k][a].v()*pb+dz[k][b].v()*pa)/Dv
        B.append(Bk)
    H=[sum(gi[a,b]*B[A][a][b] for a in range(n) for b in range(n)) for A in range(6)]
    E=[sum(Gi[a,b]*B[A][a][b] for a in range(n) for b in range(n)) for A in range(6)]
    return dict(g=g,gi=gi,R=R,G=Gi,H=H,E=E,B=B,D=Dv)

def mx(v): return max(abs(e) for e in v)
def nhat_sph(a,b):
    d=1+a*a+b*b; return [2*a/d,2*b/d,(1-a*a-b*b)/d]
def sph_chart(u,v,wJ,wbJ):
    """Cartesian M^4 from u,v and w, wbar jets (w need not be a chart variable)."""
    t=(u+v)*(mp.mpf(1)/2); r=(v-u)*(mp.mpf(1)/2); d=(1+wJ*wbJ).inv()
    return [t, r*(wJ+wbJ)*d, r*(wJ-wbJ)*d*mp.mpc(0,-1), r*(1-wJ*wbJ)*d]
