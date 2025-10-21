#!/usr/bin/env python
import sys
import csv
import numpy as np
inp = sys.argv[1]

data = []
for row in csv.reader(open(inp, 'r'), delimiter='\t'):
    data.append(row[0].split())
arr = np.array([[int(i) for i in r] for r in data])
N = arr.shape[0]
v1 = arr[np.triu_indices(N)]
v2 = arr[np.tril_indices(N)]
print(f'v1 = {v1} v2 = {v2}\nv1.v2 = {np.dot(v1,v2)}')
