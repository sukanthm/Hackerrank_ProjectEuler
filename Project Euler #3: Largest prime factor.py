#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = long(raw_input().strip())
    best = None
    factor = 2 
    while factor * factor <= n:
        while n % factor == 0:
            best = factor
            n //= factor
        factor += 1
    if (n > 1):
        print n
    else:
        print best
