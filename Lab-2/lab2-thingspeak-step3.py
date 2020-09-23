import urllib
import requests
import json

Results = 1
KEY = 'XKIVZHPABVP815EY'
CHANNEL = '1155817'
URL = 'https://api.thingspeak.com/channels/'+CHANNEL+'/feeds.json?api_key='+KEY+'&results='+str(Results)

Data = requests.get(URL).json()
ChannelName = Data['channel']['name']
ChannelID = Data['channel']['id']

Feeds = Data['feeds']
Temperature = []

for x in Feeds:
	Temperature.append(x['field1'])
	
print('Name: '+ChannelName)
print('ID: '+str(ChannelID))
print('Temperature: '+str(Temperature))
