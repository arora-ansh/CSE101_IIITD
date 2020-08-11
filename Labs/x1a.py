import urllib.request

a=urllib.request.urlopen("https://api.exchangeratesapi.io/latest")
json=a.read()



arr=[]
x=12
y=16
z=17
w=24
data=str(json)
end=data.find('}')
while True:
	cur=data[x+1:y]
	val=float(data[z+1:w])
	arr.append([cur,val])
	x=data.find('"',y+1)
	y=data.find('"',x+1)
	z=data.find(':',z+1)
	w=data.find(',',w+1)
	if z==end-5 or z==end-6 or z==end-7 or z==end-8 :
		cur=data[z-4:z-1]
		val=float(data[z+1:end])
		arr.append([cur,val])
		break
print(arr)
n=len(arr)
print(n)

for i in range(n):
    for j in range(0, n-i-1):
        if arr[j][1]>arr[j+1][1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)

for i in range(n):
    print("1 euro =",arr[i][1],arr[i][0])
