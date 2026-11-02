# Normal volume flux at degenerate 3-surfaces, and the field equation at det g4 = 0.
import sympy as sp

print("=== A. Local block: g_ss=A, g_sv=B, g_vv=C, D=AC-B^2, v>0 ===")
v = sp.symbols('v', positive=True)
a, b, c = sp.symbols('a b c', positive=True)
cases = [
    ("regular null   A=a v,    B=b      ", a*v, b),
    ("d=1 simple     A=a v,    B=b v    ", a*v, b*v),
    ("d=1 non-smooth A=a v,    B=b v^1/2", a*v, b*sp.sqrt(v)),
    ("d=2 double     A=a v^2,  B=b v    ", a*v**2, b*v),
    ("d=3 odd        A=a v^3,  B=b v^2  ", a*v**3, b*v**2),
    ("d=4 even       A=a v^4,  B=b v^2  ", a*v**4, b*v**2),
]
for name, A, B in cases:
    C = -c
    D = sp.simplify(A*C - B**2)
    # inverse block
    gvv = A/D
    gvs = -B/D
    gss = C/D
    sq = sp.sqrt(sp.Abs(D))
    lim_vv = sp.limit(sq*gvv, v, 0)
    lim_vs = sp.limit(sq*gvs, v, 0)
    print(name, "| sqrt|D| g^vv ->", lim_vv, "| sqrt|D| g^vs ->", sp.simplify(lim_vs))

print()
print("=== B. Graph xi=f(m): field equation of the hypersurface in M4 x S1 ===")
t, x, y, z = sp.symbols('t x y z', real=True)
X = (t, x, y, z)
eta = sp.diag(1, -1, -1, -1)
f = sp.Function('f')(t, x, y)
fd = [sp.diff(f, q) for q in X]
fu = [eta[i, i]*fd[i] for i in range(4)]
F = sum(fu[i]*fd[i] for i in range(4)) - 1
box = sum(eta[i, i]*sp.diff(f, X[i], 2) for i in range(4))
fab = sum(fu[i]*fu[j]*sp.diff(f, X[i], X[j]) for i in range(4) for j in range(4))
# d_a ( f^a / sqrt(s F) ), s=+1 for F>0 written with a symbol that avoids branch choices
FF = sp.Symbol('FF', positive=True)
div = sum(sp.diff(fu[i], X[i]) for i in range(4))/sp.sqrt(F) \
    - sp.Rational(1, 2)*sum(fu[i]*sp.diff(F, X[i]) for i in range(4))/F**sp.Rational(3, 2)
target = (F*box - fab)/F**sp.Rational(3, 2)
print("d_a(f^a/sqrt F) - (F box f - f^a f^b f_ab)/F^(3/2) =", sp.simplify(div - target))
gradn = sum(fu[i]*sp.diff(F, X[i]) for i in range(4))
print("f^a d_a F - 2 f^a f^b f_ab =", sp.simplify(gradn - 2*fab))
print("Hence at F=0 with finite box f: f^a d_a F = 0, the kernel n=grad f is tangent to F=0.")

print()
print("--- exact check on xi = a eta + n theta (rata-virta) in Cartesian coordinates ---")
aa, nn = sp.symbols('a n', positive=True)
f2 = aa*sp.atanh(t/x) + nn*sp.atan2(z, y)
fd2 = [sp.diff(f2, q) for q in X]
fu2 = [eta[i, i]*fd2[i] for i in range(4)]
F2 = sum(fu2[i]*fd2[i] for i in range(4)) - 1
box2 = sum(eta[i, i]*sp.diff(f2, X[i], 2) for i in range(4))
fab2 = sum(fu2[i]*fu2[j]*sp.diff(f2, X[i], X[j]) for i in range(4) for j in range(4))
print("F box f - f^a f^b f_ab =", sp.simplify(F2*box2 - fab2))

print()
print("--- non-null det=0 surface fails: xi = x^2/2 + c*x with F=-(x+c)^2-1 never zero; use xi=t^2/2 ---")
f3 = t**2/2
F3 = sp.diff(f3, t)**2 - 1
print("F=", F3, " F box f - f^a f^b f_ab =", sp.simplify(F3*sp.diff(f3, t, 2) - sp.diff(f3, t)**2*sp.diff(f3, t, 2)))
print("Nonzero constant -1: a surface with kernel normal to F=0 does not solve the equation.")

print()
print("=== C. General codimension, chart with kernel e=d_v transverse to X3={v=0} ===")
al, kk = sp.symbols('alpha K', positive=True)
sg = sp.sqrt(al*v)            # sqrt|g| up to the smooth factor sqrt|q|
ginv = 1/(al*v)               # g^vv
lead = sp.diff(sg*ginv, v)    # coefficient of d_v h^k at leading order
print("d_v( sqrt|g| g^vv ) =", sp.simplify(lead), " ~ v^(-3/2), so d_v h^k = 0 would be forced")
print("The H Christoffel term and the cross terms are O(v^(-1/2)), checked by power counting in the note.")
