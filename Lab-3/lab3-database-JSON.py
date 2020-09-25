import urllib
import requests
import datetime
import sqlite3

# The URL that is formatted:
#http://api.openweathermap.org/data/2.5/weather?APPID=a808bbf30202728efca23e099a4eecc7&units=imperial&q=ottawa
# As of October 2015, you need an API key.
# I have registered under my Carleton email.

apiKey = "a808bbf30202728efca23e099a4eecc7" # If it doesn’t work, get your own.

# Query the user for a city
city = input("Enter the name of a city whose weather you want: ")

url = "http://api.openweathermap.org/data/2.5/weather?APPID="+apiKey+"&units=imperial&q="+city
#print (url)

data = requests.get(url).json()
#print (data)

temperature = data['main']['temp']
humidity = data['main']['humidity']
pressure = data['main']['pressure']
wind = data['wind']['speed']

print ("Temperature: %d%sF" % (temperature, chr(176)))
print ("Humidity: %d%%" % humidity)
print ("Pressure: %d" % pressure )
print ("Wind : %d" % wind)

db = sqlite3.connect("weather.db");
db.row_factory = sqlite3.Row
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS weather(time TEXT, location TEXT, temperature INTEGER, humidity INTEGER, pressure INTEGER, wind INTEGER);")
cursor.execute("insert into weather values ('"+str(datetime.datetime.now())+"', '"+city+"', "+str(temperature)+", "+str(humidity)+", "+str(pressure)+", "+str(wind)+");")
db.commit()
db.close()