#!/usr/bin/env python3

import json
import requests
import sys
from datetime import datetime
from dateutil.parser import parse
from dateutil import tz

"""
Some bus stops near UNSW:
  * 203115: High Street near Gate 9 (All buses except 891)
  * 203116: High Street near Gate 9 (891 UNSW to Central)
  * 203121: High Street near Gate 3
  * 203114: High Street opp. Randwick Racecourse
  * 203220: Anzac Parade near Barker Street

"""

api_endpoint = "https://api.transport.nsw.gov.au/v1/tp/"
apikey_file_location = "./apikey"
highstreet_bus_stop = '203116'
local_timezone = tz.tzlocal()

def getApiKey(filename="./apikey"):
    apikey = None
    try:
        with open (apikey_file_location) as f:
            apikey = f.read().rstrip()
    except Exception as err:
        raise # let whatever function called this deal with the error
    return apikey

def getDepartures(stop_id=highstreet_bus_stop):
    """Gets departure times from a specific bus stop"""

    apicall = "departure_mon"
    apikey = getApiKey()
    if apikey is None:
        return None

    try:
        apikey = getApiKey()
    except Exception as err:
        raise # not my problem lol

    when = datetime.now()

    # build http header
    header = {'Authorization': "apikey " + apikey}

    # build request parameters
    parameters = {
        'outputFormat': 'rapidJSON',
        'coordOutputFormat': 'EPSG:4326',
        'mode': 'direct',
        'type_dm': 'stop',
        'name_dm': stop_id,
        'depArrMacro': 'dep',
        'itdDate': when.strftime("%Y%m%d"),
        'itdTime': when.strftime("%H%M"),
        'TfNSWDM': 'true'
    }

    url = api_endpoint + apicall

    # send HTTP request and receive response
    response = requests.get(url, parameters, headers=header)
    response = response.json()

    # Get actual stop and departure data if exists
    stopEvents = None
    if 'stopEvents' in response:
        stopEvents = response['stopEvents']

    return stopEvents

def printService (plannedDep, estDep, route_id, route_desc):
    """Format and print service departure times."""
    print ('---')
    infoStr = "%s %s\n %s: %s" % (plannedDep, estDep, route_id, route_desc)
    print (infoStr)

def main(args):
    """Main function."""
    stop_id = highstreet_bus_stop
    if len(args[1:]) > 0: # get bus stop ID from args if provided
        stop_id = args[1]

    departures = None
    try:
        departures = getDepartures(stop_id)
    except IOError as err:
        print ("IO Exception occurred")
        print (err)
    except Exception as err:
        print ("An error has occurred")
        print (err)

    if departures is None:
        print ("No departures available")
        sys.exit()

    for departure in departures:

        # parse planned and estimated departure times
        plannedDeparture = parse(departure['departureTimePlanned'])
        plannedDeparture = plannedDeparture.astimezone(local_timezone)
        estimatedDeparture = plannedDeparture
        if 'departureTimeEstimated' in departure:
            estimatedDeparture = parse(departure['departureTimeEstimated'])
            estimatedDeparture = estimatedDeparture.astimezone(local_timezone)

        transportation = departure['transportation']
        route_id = transportation['number']
        route_desc = transportation['description']
        printService (plannedDeparture, estimatedDeparture, route_id, route_desc)

if __name__ == "__main__":
    main(sys.argv)
