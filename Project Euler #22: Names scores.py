N1=int(raw_input().strip())
N=[]
for t in xrange(N1):
    N.append(raw_input().strip())

N.sort()
    
Q1=int(raw_input().strip())
for t in xrange(Q1):
    q=raw_input().strip()
    print (1+N.index(q))*sum([ord(x)-64 for x in q])
