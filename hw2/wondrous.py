#!/usr/bin/env python
import sys
inp = sys.argv[1]
if not inp.isnumeric():
    print(f"'{inp}' is not an integer.")
    sys.exit()
i = int(inp)
if i==0:
    print(f"0 is not a valid integer")
    sys.exit()
steps = 0
while i>1:
    steps+=1
    if (i % 2) == 0:   #even
        i/=2
    else:    #odd
        i*=3
        i+=1
if i == 1:
    print(f'{inp} is wondrous. It converges in {steps} steps.')
else:
    print(f'{inp} is unwondrous. It converges to {i} in {steps} steps.')