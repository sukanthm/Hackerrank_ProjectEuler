#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    s=0
    for x in reversed(range(101101,n)):
      if str(x)[:3]==str(x)[3:][::-1]:
        for y in range(100,1000):
          if x%y==0 and len(str(x//y))==3:
            print(x)
            s=1
            break
      if s:
        break
      else:
        pass
