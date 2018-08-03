#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    N = [x for x in range(1,n + 1)]
    s=1
    while sum(N)>n:
        i = min(list(set(N) - set([1])))
        N1 = [x / i if x%i==0 else x for x in N]
        if N1!=N:
            s*=i
            N=N1
    print s
