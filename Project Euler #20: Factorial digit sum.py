from math import factorial
T=int(raw_input().strip())
for t in xrange(T):
    print sum(map(int,list(str(factorial(int(raw_input().strip()))))))
