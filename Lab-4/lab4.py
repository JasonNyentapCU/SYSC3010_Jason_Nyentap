import http.client
import urllib
import time

key = "7481QW0APO2BO2BU"  #API Key
group = "L1-F-8"
identifier = "C"
email = "jasonnyentap@cmail.carleton.ca"

params = urllib.parse.urlencode({'field1': group, 'field2': identifier, 'field3': email, 'key':key }) 
headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
conn = http.client.HTTPConnection("api.thingspeak.com:80")
try:
	conn.request("POST", "/update", params, headers)
	response = conn.getresponse()
	print(response.status, response.reason)
	data = response.read()
	conn.close()
except:
	print("connection failed")