#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = long(raw_input().strip())
    a,b,s=1,1,0
    while a<n:
        if a%2==0:
            s+=a
        a,b=a+b,a
    print s
