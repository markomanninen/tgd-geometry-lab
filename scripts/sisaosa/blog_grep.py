import json,re,sys
d=json.load(open(sys.argv[1]))
pats=[r'(CP.?2|CP_2)[- ]type[^.]{0,200}(energy|mass|momentum)',r'(energy|mass|four-momentum)[^.]{0,120}(CP.?2|CP_2)[- ]type',r'(3-D|4-D|3-dimensional|4-dimensional|three-dimensional|four-dimensional)[^.]{0,20} mass',r'mass[^.]{0,40}(3-D|4-D)\b',r'light-like geodesic',r'scalar curvature[^.]{0,120}(action|volume)',r'curvature scalar[^.]{0,120}(action|volume)',r'p-adic mass[^.]{0,120}(Euclidean|wormhole|CP.?2)']
seen=0
for e in d:
    if e['d']<'2016': continue
    c=e['c']
    for p in pats:
        for m in re.finditer(p,c):
            a=max(0,m.start()-120);b=min(len(c),m.end()+160)
            print(e['d'],'|',e['t'][:50],'|',c[a:b].replace('\n',' '));seen+=1
            break
print(seen)
