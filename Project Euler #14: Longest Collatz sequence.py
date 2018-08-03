T=int(raw_input().strip())
N=[]
for t in xrange(T):
    N.append(int(raw_input().strip()))

C=[0]
B=[]
count_max=0
for i in xrange(2,max(N)+1):
    count=0
    i1=i
    x=len(C)
    while i1 > x:
        count+=1;
        if i1%2==0: i1/=2; 
        else: i1=i1*3+1;
    if i1>1: count+=C[i1-1]
    C.append(count)
    if count>=count_max: B.append(i); count_max=count;

for n in N:
    print [b for b in B if b<=n][-1]
