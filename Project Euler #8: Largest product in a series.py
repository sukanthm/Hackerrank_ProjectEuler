#!/bin/python

import sys
from operator import mul

t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = raw_input().strip()
    max=0
    for i in range(n-k+1):
        if max<reduce(mul,map(int,str(num)[i:i+k]),1):
            max = reduce(mul, map(int, str(num)[i:i + k]), 1)
    print max
    
