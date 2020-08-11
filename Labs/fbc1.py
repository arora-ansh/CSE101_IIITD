import math
def solution(area):
    # Your code here
    arr = []

    while True:
	    t = math.sqrt(area)
	    u = math.floor(t)
	    #print(u*u)
	    arr.append(u*u)
	    area = area - (u*u)
	    if(area<=0):
		    break
	print("		")
    for i in range(len(arr)):
        if(i<len(arr)-1):
            print(arr[i], end=",")
        else:
            print(arr[i])
solution(12)
solution(15324)