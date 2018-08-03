from math import factorial
T=int(raw_input().strip())
for t in xrange(T):
    X=raw_input().strip().split(' ')
    n=int(X[0]); m=int(X[1]);
    print (factorial(m+n)/(factorial(m)*factorial(n)))%(10**9+7)
