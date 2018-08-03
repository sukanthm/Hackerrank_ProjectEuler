T=int(raw_input().strip())
for t in xrange(T):
    N=int(raw_input().strip())
    A=[]
    for n in xrange(N):
        A.append(map(int,raw_input().strip().split(' ')))
    a=[[0]]
    for i in xrange(1,n+1):
        b=[]
        for j in a[-1*(2**(i-1)):]:
            b.append(j+[j[-1]])
            b.append(j+[j[-1]+1])
        a=a+b
    a=a[-1*(2**(n)):]
    max_sum=0
    for a1 in a:
        sum_current=0
        for x,y in enumerate(a1):
            sum_current+=A[x][y]
        if max_sum<sum_current : max_sum=sum_current;
    print max_sum
