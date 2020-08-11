q=int(input())
a=[]

def ps(A):
    if A==[]:
        return [[]]
    a=A[0]
    ips = ps(A[1:])
    r=[]
    for s in ips:
        r.append([a]+s)
    return r + ips

for i in range(q):
    x=input()
    a.append(x)

for k in range(q):
    b=[]
    for j in range(len(a[i])):
        x=a[i][j]
        b.append(x)
    fin=ps(b)
    print(fin)
    def s(k,x):
        for i in range(len(x)):
            if k==x[i]:
                return(0)
            else:
                return(-1)
        
    key=0
    c=[]
    for i in range(len(fin)):
        for j in range(i+1,len(fin)):
            fin1=sorted(fin[i])
            fin2=sorted(fin[j])
            x=s(fin1,c)
            if fin1==fin2 and x!=0:
                c.append(fin1)                    
                key=key+1
    

    print(key)
        
        
