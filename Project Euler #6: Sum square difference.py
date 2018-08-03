#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    print (n*(n+1)//2)**2-n*(n+1)*(2*n+1)//6
    
