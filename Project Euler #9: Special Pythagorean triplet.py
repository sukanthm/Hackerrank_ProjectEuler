#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    x=[-1]
    for a in xrange(1,n//2):
        if (n*n-2*a*n)%(2*(n-a))==0:
            b = (n*n-2*a*n)/(2*(n-a))
        else:
            continue
        c = n - a - b
        x.append(int(a*b*c))
    print max(x)
