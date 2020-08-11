# Name : Ansh Arora
# Roll No : 2019022
# Group : 4

import urllib
import requests
from datetime import *

def getLatestRates():
	""" Returns: a JSON string that is a response to a latest rates query.

	The Json string will have the attributes: rates, base and date (yyyy-mm-dd).
	"""
	link="https://api.exchangeratesapi.io/latest"
	a=urllib.request.urlopen(link)
	data = a.read()
	return data 							#Simply returns data in the json string that it extracts after the read() function.

def changeBase(amount, currency, desiredCurrency, date):
	""" Outputs: a float value f.
	"""

	link = "https://api.exchangeratesapi.io/"+date 					#Assigns the date given as argument in the API call
	a=urllib.request.urlopen(link)
	data = str(a.read())
	data=data[2:-1]							#Gets the string to get converted into a form that can directly be converted to dictionary
	dic=eval(data)							#Converts the string into dictionary
	x=dic['rates']							#Gets the rates out from the dcitionary
	if currency=="EUR":						#Condition applied to deal with EUR corner case
		cur1=1
		
	else:
		cur1=x[currency]

	if desiredCurrency=="EUR":
		cur2=1

	else:
		cur2=x[desiredCurrency]
	return amount*(cur2/cur1)				#Simply returns the final value


def printAscending(json):
	""" Output: the sorted order of the Rates 
		You don't have to return anything.
	
	Parameter:
	json: a json string to parse
	"""

	arr=[]									#Declared an array
	x=12									#For string operations, given starting values to 4 variables
	y=16
	z=17
	w=24
	data=str(json)							
	end=data.find('}')
	while True:								#Runs a loop to get a 2 dim list, where the 1st column is for the currency, 
		cur=data[x+1:y]						#while the second column just gives the currency's value
		val=float(data[z+1:w])
		arr.append([cur,val])
		x=data.find('"',y+1)
		y=data.find('"',x+1)				#Filling up the list here
		z=data.find(':',z+1)
		w=data.find(',',w+1)
		if z==end-5 or z==end-6 or z==end-7 or z==end-8 :
			cur=data[z-4:z-1]
			val=float(data[z+1:end])
			arr.append([cur,val])
			break

	n=len(arr)											#Have used bubble sort to sort the currencies in increasing order.
	for i in range(n):
		for j in range(0,n-i-1):
			if arr[j][1]>arr[j+1][1]:
				arr[j],arr[j+1]=arr[j+1],arr[j]

	for i in range(n):
		print("1 Euro =",arr[i][1],arr[i][0])			#For loop to print the finally ordered list


def extremeFridays(startDate, endDate, currency):
	""" Output: on which friday was currency the strongest and on which was it the weakest.
		You don't have to return anything.
		
	Parameters: 
	stardDate and endDate: strings of the form yyyy-mm-dd
	currency: a string representing the currency those extremes you have to determine
	"""

	start=datetime(int(startDate[:4]),int(startDate[5:7]),int(startDate[8:]))			#Start and end alloted datetime type values
	end=datetime(int(endDate[:4]),int(endDate[5:7]),int(endDate[8:]))
	a=start
	datex=a

	while True:												#Loop to find out the first Friday in the given
		if datex.weekday()==4:
			break
		else:
			datex=datex+timedelta(days=1)

	datemin=datex 											#Given inital values to datemin and datemax, variables that'll hold the final answer dates
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
	minrate=ym 												#Given inital values and minrate and maxrate, variables that'll hold the final answer's
	maxrate=ym

	while True:
		date=str(datex)[:10]
		link="https://api.exchangeratesapi.io/"+date 		#Have run a loop to test each 7th day from the first friday, i.e. all Fridays seperately and find out the answer
		a=urllib.request.urlopen(link)
		data=str(a.read())
		data=data[2:-1]
		dd=eval(data)
		x=dd['rates']
		y=x[currency]										#Find out the valiue of the currency on that particular Friday
		if y>minrate:										#If value greater than minrate, new minrate and datemin are alloted, similarly for max case
			minrate=y
			datemin=datex
		elif y<maxrate:
			maxrate=y
			datemax=datex

		datex=datex+timedelta(days=7)						# Takes to the next Friday

		if end<datex:										# Breaks the loop if final date is breached
			break

	print(currency,"was strongest on", str(datemax)[:10],". 1 Euro was equal to", maxrate, currency)
	print(currency,"was weakest on", str(datemin)[:10],". 1 Euro was equal to", minrate, currency)


def findMissingDates(startDate, endDate):
	""" Output: the dates that are not present when you do a json query from startDate to endDate
		You don't have to return anything.

		Parameters: stardDate and endDate: strings of the form yyyy-mm-dd
	"""

	link="https://api.exchangeratesapi.io/history?start_at="+startDate+"&end_at="+endDate			#Gets a json string for all the present rate conversion strings in the range first
	x=urllib.request.urlopen(link)
	data=str(x.read())
	start=datetime(int(startDate[:4]),int(startDate[5:7]),int(startDate[8:]))
	end=datetime(int(endDate[:4]),int(endDate[5:7]),int(endDate[8:]))
	a=start
	while True: 										#Loop goes through every single day of the given range and checks whether or not it is present in the imported json string
		datex=str(a)
		datex=datex[:10]								#Used to get the date part from datetime
		if data.find(datex)==-1 :						#Find function to find if the given date string is missing or not
			print(datex)
		if a==end :
			break
		a=a+timedelta(days=1)							#Takes to next date(adds 1 day)

