i=0
def maxDistract(c1,c2,h1,h2,m):
    global i
    d1=c1/h1
    d2=c2/h2
    if d1<d2 and m>=c1:
        i=i+h1
        return maxDistract(c1,c2,h1,h2,m-c1)
    elif d1<d2 and m>=c2:
        i=i+h2
        return maxDistract(c1,c2,h1,h2,m-c2)
    elif d2<d1 and m>=c2:
        i=i+h2
        return maxDistract(c1,c2,h1,h2,m-c2)
    elif d2<d1 and m>=c1:
        i=i+h1
        return maxDistract(c1,c2,h1,h2,m-c1)
    elif d1==d2 and c1>c2:
        i=i+h2
        return maxDistract(c1,c2,h1,h2,m-c2)
    elif d1==d2 and c2>c1:
        i=i+h1
        return maxDistract(c1,c2,h1,h2,m-c1)
    else:
        return i

print(maxDistract(5,10,20,40,100))

