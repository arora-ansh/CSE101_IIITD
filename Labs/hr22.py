def help_recursion(N):
    if N==1:
        return "0"
    else:
        q = help_recursion(N-1)
        k = []
        a = ""
        for i in range(len(q)):
            if q[i]=="0":
                k=k+["01"]
            elif q[i]=="1":
                k=k+["10"]
        for i in k:
            a = a + i
        return a

a=help_recursion(6)
print(a)                
        
