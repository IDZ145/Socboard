#!/usr/bin/python2
import requests
import re
import sqlite3
from google.transit import gtfs_realtime_pb2

#There is a config file while is used to store important information such as the keys
config = open('config.txt','r')
#Looks for the api key
match = re.search("^Authorization: (.*)",config.read())
#This processes the key
key = match.group(0) 
headers = {"Authorization":match.group(0)}
bus_positions = requests.get('https://api.transport.nsw.gov.au/v1/gtfs/realtime/buses', headers=headers)
print("Retrieved {} bytes").format(len(bus_positions.content))
feed = gtfs_realtime_pb2.FeedMessage()
feed.ParseFromString(bus_positions.content)
#print(feed)
#for entity in feed.entity[0:5]:
#    print(entity)
print("Hello")
