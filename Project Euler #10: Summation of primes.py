#!/bin/python
import sys
n=[]
t = int(raw_input().strip())
for a0 in xrange(t):
    n.append(int(raw_input().strip()))

from math import sqrt
def primes(limit):
    sieve = range(limit+1); sieve[1] = 0
    for n in xrange(2, int(sqrt(limit))+1):
        if sieve[n] > 0:
            for i in xrange(n*n, limit+1, n): sieve[i] = 0
    for s,d in enumerate(sieve):
        if s>0: sieve[s]=sieve[s-1]+sieve[s]
    return sieve

x=primes(max(n))
for N in n:
    print x[N]
