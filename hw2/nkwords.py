#!/usr/bin/env python
import sys
import string
import itertools
if (len(sys.argv) != 3) or not sys.argv[1].isnumeric() or not sys.argv[2].isnumeric() or (int(sys.argv[1])==0) or (int(sys.argv[2])==0):
    print(f'Invalid input')
    sys.exit()
n = int(sys.argv[1]); k = int(sys.argv[2])
alph = list(string.ascii_uppercase)
for combo in itertools.product(alph[0:n], repeat=k):
    print(''.join(combo))