def numPairs(l,n,c):
    sum=0
    count=0
    for i in range(n):
        for j in range(n):
            sum=l[i]+l[j]
            if sum==c and i!=j:
                count=count+1

    return count

l=[2,2,1,3,4]
n=5
c=4

print(numPairs(l,n,c))
