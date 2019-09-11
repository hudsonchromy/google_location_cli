import sys
import json
import datetime
from math import sin, cos, sqrt, atan2, radians


def getDistance(long1, lat1, long2, lat2):

	long1 = radians(long1)
	long2 = radians(long2)
	lat1 = radians(lat1)
	lat2 = radians(lat2)
	R = 6373.0

	dlon = long2 - long1
	dlat = lat2 - lat1

	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
	c = 2 * atan2(sqrt(a), sqrt(1 - a))

	distance = R * c

	return distance

def printUnique(form):
	times = set()
	for time in timestamps:
		times.add(datetime.datetime.fromtimestamp(int(time)/1000).strftime(form))
	times = sorted(times)
	for time in times:
		print(time)






if (len(sys.argv) == 1 or sys.argv[1] == "help" or sys.argv[1] == "h"):
	print("Google Location CLI\n\nwithin Lattitude Longitude")

command = sys.argv[1]
if (command == "within"):
	if (len(sys.argv) < 4):
		print("Error: not enough arguements given\nNeed Command Lattitude Longitude")
	lat = sys.argv[2]
	lon = sys.argv[3]
	options = sys.argv[4:]
	dist = 1
	for item in options:
		if (item.isdigit()):
			dist = int(item)
			break
	lon = float(lon)
	lat = float(lat)
	timestamps = []
	with open('LocationHistory.json') as json_file1:
		data1 = json.load(json_file1)['locations']
	for location in data1:
		if(getDistance(location['longitudeE7'] / 10000000, location['latitudeE7'] / 10000000, lon, lat) < dist):
			timestamps.append(location['timestampMs'])
	if (len(options) == 0):
		for time in timestamps:
			print(time)
	elif ("days" in sys.argv):
		printUnique('%Y-%m-%d')
	elif ("months" in sys.argv):
		printUnique('%Y-%m')
	elif ("years" in sys.argv):
		printUnique('%Y')
	elif ("hours" in sys.argv):
		printUnique('%Y-%m-%d %H')
