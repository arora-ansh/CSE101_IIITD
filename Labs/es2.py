def search(a,low,end,key):
	mid=low+end//2
	if a[mid]==key:
		print("Found at "+(mid+1))
	elif key>a[mid]:
		search(a,mid+1,end,key)
	elif key<a[mid]:
		search(a,low,mid-1,key)



