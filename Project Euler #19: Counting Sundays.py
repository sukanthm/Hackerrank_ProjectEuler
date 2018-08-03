T=int(raw_input().strip())
for t in xrange(T):
    q1=map(int,raw_input().strip().split(' '))
    q2=map(int,raw_input().strip().split(' '))
    if q1[2]!=1:
        if q1[1]!=12:
            q1[2]=1; q1[1]+=1
        else:
            q1[2]=1; q1[1]=1;q1[0]+=1
    count=0
    while q1[0]<q2[0] or (q1[0]==q2[0] and q1[1]<=q2[1]):
        p=q1[:]
        if p[1]==1: p[1]=13; p[0]-=1;
        if p[1]==2: p[1]=14; p[0]-=1;
        x=p[0]%100;y=p[0]//100
        h=1+13*(p[1]+1)//5+(x)+(x)//4+(y)//4+(y)*5
        h=h%7
        if h==1:
            count+=1
        if q1[1]==12: q1[1]=1; q1[0]+=1
        else: q1[1]+=1
    print count
