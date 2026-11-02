#!/usr/bin/env python3
"""Numbers for G origin: p-adic R^2/G, exponential formula, n0 candidates, volume variants.
All constants CODATA 2018. hbar=c=1, K := R^2/(hbar G)."""
from math import pi, log, exp, sqrt, factorial, sin, asin
me=0.51099895e-3 # GeV
mP=1.220890e19   # GeV
p127=2**127-1
aem=1/137.035999
r=(mP/me)**2/2**127
print("(mP/me)^2 2^-127 =",r)
print("\n# Task 1a: p-adic R^2/G, m0^2 = me^2 2^127/(5+Y)")
for Y in (0,0.0317,0.5,0.7798,1):
    m0=me*2**63.5/sqrt(5+Y)
    print(f"Y={Y:<7} m0/mP={m0/mP:.4e}  R=1/m0:K={(mP/m0)**2:.4e}  R^2=3/(2m0^2):K={1.5*(mP/m0)**2:.4e}  geodesic piR (4x):K={6*(mP/m0)**2:.4e}")
print("\n# Task 1b: published or implied values of K and the Y they need")
c={ "2^24 (tgdclass1:33864)":2**24,
    "R/lP=4.167e3 (hgrtwistor:1494)":4.167e3**2,
    "x=4.2 (tgdclass2:24954)":4.2**2*1e6,
    "lP/R=2.0e-4 (tgdclass2:21052 lahella)":1/2.0e-4**2,
    "m(CP2)/mP=2.4e-4 (tgdclass2:11980)":1/2.4e-4**2,
    "eps=G/R2=4e-8 (tgdclass1:26056)":1/4e-8,
    "2.5e7 (tgdclass2:3880)":2.5e7,
    "KR Y=0 (tgdview2 taulukko 14.2)":2.5262e7,
    "K rationaali 2.4606e7":2*3*5*7*11*13*17*19*23/8*15/17,
    "tgdnumber1 ala 2.3683e7":2.3683e7,
    "n0=(7!)^2":factorial(7)**2,
    "ngr/6=60*120^3/6":60*120**3/6,
    "ngr=60*120^3 (jos h->h0)":60*120**3,
    "G/Geg=.22e-6, Geg=8R2 aK (tgdclass1:7287)":1/(8*aem*0.22e-6),
    "TG=.89e-6 (tgdclass2:3878)":1/(8*aem*0.89e-6),
}
for k,v in c.items():
    print(f"{k:48s} K={v:.5e}  (5+Y) jos R=1/m0: {v/r:.3f}  (5+Y) jos R^2=3/2m0^2: {v/r/1.5:.3f}")
print("\n# Task 1c: exponential formula hbar G = Lp^2 exp(-2a SK), Lp^2=p R^2, SK=pi/(8 aK)")
S=pi/(8*aem); print("SK(CP2)=",S," 2SK=",2*S, "exp(2SK)=",exp(2*S), " 1/gK^2=",1/(4*pi*aem))
print("K at a=1:",exp(2*S)/p127)
for K in (1.678e7,2.3683e7,2.4606e7,2.5262e7,(5040.)**2,2.92e7,7.8e7,1.01e8):
    a=log(p127*K)/(2*S)
    s4=1-a  # removed volume fraction
    rho=asin(s4**.25) if s4>0 else None
    rho2=asin((s4/2)**.25) if s4>0 else None
    print(f"K={K:.4e} a={a:.5f} 1-a={1-a:.5f} poistettu pallo rho/R={rho:.4f} kaksi palloa rho/R={rho2:.4f}")
print("dlnK/da =",2*S," -> 1% muutos a:ssa kertoo K:n luvulla",exp(0.01*2*S))
print("dlnK/d(1/aK) at a=.976 =",0.976*pi/4, "-> muutos 1/aK 137->138 kertoo K:n luvulla",exp(0.976*pi/4))
print("\n# Task 1d: same exponent without Kahler action")
K=2.5262e7
print("rho R^4 joka toistaa eksponentin: S_V=rho V=S_K kun rho R^4=1/(4 pi aK)=",1/(4*pi*aem), "(1/gK^2)")
print("S_V(CP2)/S_K(CP2) kun rho=T/(pi R^2), T=1/(8 aK R^2):",(1/(8*aem*pi))*(pi**2/2)/S)
print("twistori rho=2/(aK R1^4): R1/R kun S_V=S_K:",(8*pi)**.25, " kun T=rho pi R^2:",(16*pi)**.25)
for K in (2.5262e7,7.8e7,1.01e8):
    L=log(p127*K)
    print(f"K={K:.3e}: ln(pK)={L:.3f}; puhdas tilavuus, a=1: Lambda R^2={8*L/(pi*K):.3e}; rho R^4={L/pi**2:.3f}")
# curvature+volume: S=-(3pi/4)K(1-LR2/12) in units hbar. Fixed point of K=exp(2 a |S|)/p
for a in (1,0.976,0.5):
    K=20.
    for i in range(200): K=log(p127*K)/(2*a*3*pi/4)
    print(f"R+V, Lambda=0, a={a}: K kiintopiste {K:.3f}, R/lP={sqrt(K):.3f}")
K=2.5262e7
print("R+V: a joka antaa K=2.5262e7:",log(p127*K)/(2*3*pi/4*K))
print("\n# Task 1e: volume coefficient 1/R^4 (blog 2023-11-08): Lambda R^2=8pi/K, T=pi/R^2, ratio to 1/(8aK R^2):",pi*8*aem)
print("T G taulukko K:lla: 2.5262e7:",1/(8*aem*2.5262e7)," 7.8e7:",1/(8*aem*7.8e7)," 1.01e8:",1/(8*aem*1.01e8))
print("appendix X=(1-k2s2)s0/(aK(1-s0)): X=1 antaa s0 ~",aem/(1+aem),"; X=2.54e7 antaa 1-s0 ~",1/(aem*2.54e7))
