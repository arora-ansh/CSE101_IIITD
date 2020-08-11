N=int(input())
Fx=input()
F=Fx.split()

G=[]
for i in range(N):
    x=float(F[i])
    G.append(x)
    
W=int(input())
print(W)

arr=[0]
for i in range(N):
    for j in range(i+1,N+1):
        x=G[i:j]
        y=sum(x)
        arr.append(y)

print(arr)
n=len(arr)

key=-1

for i in range(n):
    if arr[i]==W:
        key=0

if key==0:
    print("True")
if key==-1:
    print("False")
