import sqlite3

db = sqlite3.connect("my.db");
db.row_factory = sqlite3.Row
cursor = db.cursor()
cursor.execute("insert into sensor(temperature, pressure, currentdate, currenttime) values (16, 155, '2020-09-25', '03:03:03');")
db.commit()
cursor.execute("SELECT * FROM sensor;")
for row in cursor:
	print(row['id'], row['temperature'], row['pressure'], row['currentdate'], row['currenttime'])
db.close()


db = sqlite3.connect("sensor.db");
db.row_factory = sqlite3.Row
cursor = db.cursor()
cursor.execute("CREATE TABLE sensors(sensorID INTEGER PRIMARY KEY AUTOINCREMENT, type TEXT, zone TEXT);")
cursor.execute("insert into sensors(type, zone) values ('door', 'kitchen');")
cursor.execute("insert into sensors(type, zone) values ('temperature', 'kitchen');")
cursor.execute("insert into sensors(type, zone) values ('door', 'garage');")
cursor.execute("insert into sensors(type, zone) values ('motion', 'garage');")
cursor.execute("insert into sensors(type, zone) values ('temperature', 'garage');")
db.commit()

cursor.execute("SELECT * FROM sensors WHERE zone='kitchen';")
print("Sensors in the kitchen:")
for row in cursor:
	print(row['sensorID'], row['type'])

cursor.execute("SELECT * FROM sensors WHERE type='door';")
print("Door sensors:")
for row in cursor:
	print(row['sensorID'], row['zone'])
db.close()