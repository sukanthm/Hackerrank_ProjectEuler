#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())-1
    x3 = n//3
    x5 = n//5
    x15 = n//15
    sum1 = 3*x3*(x3+1)
    sum2 = 5*x5*(x5+1)
    sum3 = 15*x15*(x15+1)
    print long((sum1+sum2-sum3)/2)
    
