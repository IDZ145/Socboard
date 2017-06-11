#!/usr/bin/env python3

# Response class
# [{
#   "route_id": "string",
#   "stop_name": "string",
#   "stop_location_coords": [
#     123.45,
#     67,890
#   ],
#   "planned_depart_time": "string",
#   "estimated_depart_time": "string",
#   "crowded_level": 2,
# }]

def getHighStTestData():
    depart1 = {
        "route_id": "400",
        "stop_name": "High St near Gate 9 UNSW",
        "stop_location_coords": [
            -33.916,
            151.23337
        ],
        "planned_depart_time": "2017-06-11 19:01:00",
        "estimated_depart_time": "2017-06-11 19:03:00",
        "description": "Bondi Junction to Burwood via Eastgardens (Limited Stops)",
        "crowded_level": 1
    }
    depart2 = {
        "route_id": "370",
        "stop_name": "High St near Gate 9 UNSW",
        "stop_location_coords": [
            -33.916,
            151.23337
        ],
        "planned_depart_time": "2017-06-11 19:08:00",
        "estimated_depart_time": "2017-06-11 19:10:00",
        "description": "Coogee to Leichhardt Marketplace",
        "crowded_level": 1
    }
    depart3 = {
        "route_id": "348",
        "stop_name": "High St near Gate 9 UNSW",
        "stop_location_coords": [
            -33.916,
            151.23337
        ],
        "planned_depart_time": "2017-06-11 19:19:00",
        "estimated_depart_time": "2017-06-11 19:19:00",
        "description": "Bondi Junction to Wolli Creek",
        "crowded_level": 1
    }

    departure_list = [depart1, depart2, depart3]

    return departure_list
def getAnzacPdeTestData():
    return ""

def getBusesExpressTestData():
    return ""
