tempx = input().split()
n = int(tempx[0])
m = int(tempx[1])
dict = {}
for case in range(m):
	temp = input().split()
	if temp[0] in dict.keys():
		dict[temp[0]][0]=dict[temp[0]][0]+1
		dict[temp[0]][1]+=int(temp[1])
	else:
		dict[temp[0]] = [1,int(temp[1])]
x = dict['BhayanakMaut'][0]
y = dict['BhayanakMaut'][1]
ans = 1
for i in dict:
	if(i!='BhayanakMaut' and dict[i][0]>x):
		ans = ans + 1
	elif(i!='BhayanakMaut' and dict[i][0]==x and dict[i][1]<y):
		ans = ans + 1
print(ans)
