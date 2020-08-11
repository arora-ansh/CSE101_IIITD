import urllib
import requests
from datetime import *

currency = "INR"
startDate = "2017-01-01"
endDate = "2017-12-31"


start=datetime(int(startDate[:4]),int(startDate[5:7]),int(startDate[8:]))
end=datetime(int(endDate[:4]),int(endDate[5:7]),int(endDate[8:]))
a=start
datex=a

while True:
	if a.weekday()==4:
		datex=a
                break
	else:
		datex=datex+timedelta(days=1)
		
	datemin=datex
	datemax=datex
	d=str(datex)[:10]
	link="https://api.exchangeratesapi.io/"+d
	m=urllib.request.urlopen(d)
	datam=str(m.read())
	datam=datam[2:-1]
	ddm=eval(datam)
	xm=dd['rates']
	ym=x[currency]
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

    	if end==date:
    		break
    	datex=datex+timedelta(days=7)

print(currency,"was strongest on", str(datemax)[:10],". 1 Euro was equal to", maxrate, currency)
print(currency,"was weakest on", str(datemin)[:10],". 1 Euro was equal to", minrate, currency)
