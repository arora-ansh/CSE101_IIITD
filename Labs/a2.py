import urllib
import requests

link = "https://api.exchangeratesapi.io/latest"

a = urllib.request.urlopen(link)
data = a.read()