def sw(x,k):
    key=0
    a=[]
    for i in range(len(x)):
        m=int(x[i])
        a.append(m)
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if key>k:
                break
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
                key=key+1
    return a

x=input()
k=int(input())
a=sw(x,k)

for i in range(len(a)):
    print(a[i],end="")
                
            
