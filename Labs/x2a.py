import urllib
import requests
from datetime import *

def findMissingDates(startDate, endDate):

	link="https://api.exchangeratesapi.io/history?start_at="+startDate+"&end_at="+endDate
	a=urllib.request.urlopen(link)
	data=str(a.read())
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
		
findMissingDates("2019-01-01", "2019-01-31")
