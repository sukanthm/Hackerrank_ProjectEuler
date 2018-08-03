#!/bin/python

import sys
n=[]
t = int(raw_input().strip())
for a0 in xrange(t):
    n.append(int(raw_input().strip()))

p = [2, 3]
i = 5
while len(p) < max(n):
    flag = 0
    for j in p:
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        p.append(i)
    i += 2

for x in n:
    print p[x-1]
