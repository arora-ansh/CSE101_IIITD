import urllib.request
link = "https://api.exchangeratesapi.io/latest"
a = urllib.request.urlopen(link)
b = a.read()
