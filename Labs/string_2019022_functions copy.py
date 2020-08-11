def get_every_fourth(S):
    x=S.strip()
    y=x[-1::-4]
    z=y[::-1]
    return(z)

def get_every_kth(s,k,i):
    x=s.strip()
    y=x[i::-k]
    z=y[::-1]
    return(z)

def decode_string(s):
    x=s.strip()
    y=x[::-1]
    a=y.find('_')
    b=y.find('_',(a+1))
    z=y[a+1:b]
    w=z[::-1]
    return(w)

    

