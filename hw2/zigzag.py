#!/usr/bin/env python
import sys
import itertools
inp = sys.argv[1]
if not inp.isnumeric():
    print(f'{inp} is not an integer.')
    sys.exit()
    
N = int(inp)
set = list(range(1,N+1))
combos =[]
for combo in itertools.permutations(set):
    combos.append(list(combo))
    
alt_perms = 0
for com in combos:
    alt1=0 # 0 > 1 < 2 ...
    alt2=0 # 0 < 1 > 2 ...
    for i in range(1, N): # if N = 5, this will parse i = 1 to 4 
        if i%2 ==1: #odd index
            if com[i-1]>com[i]:
                alt1+=1
            else:
                alt2+=1
        else: #even index
            if com[i-1]>com[i]:
                alt2+=1
            else:
                alt1+=1
    if alt1==(N-1) or alt2==(N-1):
        alt_perms+=1

print(f'{alt_perms} {len(combos)} {(alt_perms/len(combos)):.6f}')
    
            
                
        