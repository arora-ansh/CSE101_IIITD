A=input()
B=input()
arrA=[]
arrB=[]

print(A)
print(B)

for i in range(len(A)):
    x=A[i]
    arrA.append(x)

for i in range(len(B)):
    x=B[i]
    arrB.append(x)

xA=[]
xB=[]

for i in range(len(arrA)):
    for j in range(i+1,len(arrA)+1):
        x=arrA[i:j]
        xA.append(x)

for i in range(len(arrB)):
    for j in range(i+1,len(arrB)+1):
        x=arrB[i:j]
        xB.append(x)

print(xA)
print(xB)

maxlen=0

for i in range(len(xA)):
    for j in range(len(xB)):
        if xA[i]==xB[j]:
            l=len(xA[i])
            if l>maxlen:
                maxlen=l
                
print(maxlen)
