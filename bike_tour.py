def pick(x,n,u):
    m=0
    for i in range(2,len(x)):
        p=x[i-1]
        if p>x[i-1-1] and p> x[i]:
            m=m+1
        else:
            continue
    return m
     

y=int(input())
u=0
for i in range(y):
    n=int(input())
    u=u+1
    x=[int(i) for i in input().split()]
    m=pick(x,n,u)
    print("Case #{}: {}".format(u,m))
     

         
     
    


