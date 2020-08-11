def does_it_divide(nn,l):
    su=0
    product=1
    for i in l:
        su = su+i
    for j in l:
        product=product*j

    if product%su==0:
        return "YES"
    else:
        return "NO"

does_it_divide(3,[1,2,3,7,8])


