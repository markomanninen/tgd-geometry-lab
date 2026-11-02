# Flux of d Psi on CP2 with tubes Theta<eps, Theta>pi-eps, r>rm removed (R=1). Psi is harmonic, Neumann on the tubes.
import mpmath as mp
def num(eps,rm):
    I=lambda r,t: r*(r**2*mp.sin(t)+1/mp.sin(t))/(2*(1+r**2)**2)
    return 2*mp.pi*mp.quad(lambda r: mp.quad(lambda t:I(r,t),[eps,mp.pi/2,mp.pi-eps]),[0,1,rm])
def cl(eps,rm):
    F=1+rm**2
    return mp.pi*(mp.log(F)+1/F-1+(1-1/F)*mp.log(mp.cot(eps/2)))
for eps,rm in [(0.3,3),(0.1,10),(0.5,2)]:
    print(eps,rm,num(mp.mpf(eps),mp.mpf(rm)),cl(mp.mpf(eps),mp.mpf(rm)))
