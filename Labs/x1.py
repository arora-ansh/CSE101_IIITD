import urllib
import requests
from datetime import *

def getLatestRates():

	"""Returns JSON string from query"""

	link="https://api.exchangeratesapi.io/latest"
	a=urllib.request.urlopen(link)
	data = a.read()
	return data

def changeBase(amount, currency, desiredCurrency, date):

	link = "https://api.exchangeratesapi.io/"+date
	a=urllib.request.urlopen(link)
	data = str(a.read())
	data=data[2:-1]
	dic=eval(data)
	x=dic['rates']
	if currency=="EUR":
		cur1=1
		
	else:
		cur1=x[currency]

	if desiredCurrency=="EUR":
		cur2=1

	else:
		cur2=x[desiredCurrency]
	return amount*(cur2/cur1)

def printAscending(json):

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

	n=len(arr)
	for i in range(n):
		for j in range(0,n-i-1):
			if arr[j][1]>arr[j+1][1]:
				arr[j],arr[j+1]=arr[j+1],arr[j]

	for i in range(n):
		print("1 Euro =",arr[i][1],arr[i][0])

def extremeFridays(startDate, endDate, currency):

	start=datetime(int(startDate[:4]),int(startDate[5:7]),int(startDate[8:]))
	end=datetime(int(endDate[:4]),int(endDate[5:7]),int(endDate[8:]))
	a=start
	datex=a

	while True:
		if datex.weekday()==4:
			break
		else:
			datex=datex+timedelta(days=1)

	datemin=datex
	datemax=datex
	d=str(datex)
	d=d[:10]
	link="https://api.exchangeratesapi.io/"+d
	m=urllib.request.urlopen(link)
	datam=str(m.read())
	datam=datam[2:-1]
	ddm=eval(datam)
	xm=ddm['rates']
	ym=xm[currency]
	minrate=ym
	maxrate=ym

	while True:
		date=str(datex)[:10]
		link="https://api.exchangeratesapi.io/"+date
		a=urllib.request.urlopen(link)
		data=str(a.read())
		data=data[2:-1]
		dd=eval(data)
		x=dd['rates']
		y=x[currency]
		if y>minrate:
			minrate=y
			datemin=datex
		elif y<maxrate:
			maxrate=y
			datemax=datex

		datex=datex+timedelta(days=7)

		if end<datex:
			break

	print(currency,"was strongest on", str(datemax)[:10],". 1 Euro was equal to", maxrate, currency)
	print(currency,"was weakest on", str(datemin)[:10],". 1 Euro was equal to", minrate, currency)




def findMissingDates(startDate, endDate):

	link="https://api.exchangeratesapi.io/history?start_at="+startDate+"&end_at="+endDate
	x=urllib.request.urlopen(link)
	data=str(x.read())
	start=datetime(int(startDate[:4]),int(startDate[5:7]),int(startDate[8:]))
	end=datetime(int(endDate[:4]),int(endDate[5:7]),int(endDate[8:]))
	a=start
	while True:
		datex=str(a)
		datex=datex[:10]
		if data.find(datex)==-1 :
			print(datex)
		if a==end :
			break
		a=a+timedelta(days=1)



	

	






	


