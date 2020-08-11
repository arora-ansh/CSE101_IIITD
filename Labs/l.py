def x(y):
    a=y.find(" ")
    i=a
    while True:
        b=y.find(" ",i+1)
        if y[b+1]!=" ":
            break

    print(y[b:]+"_"+y[:a+1])

y=input()
x(y)
        
