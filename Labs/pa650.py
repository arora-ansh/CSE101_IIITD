t = int(input())
for case in range(t):
	s = input()
	n = len(s)
	arr = []
	arr.append(s[0])
	i=2
	while i<n:
		arr.append(s[i])
		i=i+2
	arr.append(s[n-1])
	for i in arr:
		print(i,end="")
	print()
