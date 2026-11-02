import importlib.util,sys,io,contextlib,numpy as np
src=open('reuna_vakaus_2_kuutio.py').read().split("print('Fermat and family")[0]
exec(src)
tail=open('reuna_vakaus_2_kuutio.py').read().split('# spectrum of -Delta')[1]
exec('# '+tail.split("print('Lambda KK")[0])
for L,KK in [(3.0,14),(3.0,20),(3.9,20),(3.9,26)]:
    print(L,KK,spec(L,KK,256),flush=True)
g=geom(0.0,512,512); K=g['K']; i=np.unravel_index(K.argmin(),K.shape); print('Kmin',K.min())
