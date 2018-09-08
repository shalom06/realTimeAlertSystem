#created By -Shalom Mathews

import proximitypyhash as ppyh
import math

import requests

import pyrebase

import json



config = {
  "apiKey": "AIzaSyAAHBVmQ7LdMJPgyeespjctd3cdV5snCAw",
  "authDomain": "webapp-5eb06.firebaseapp.com",
  "databaseURL": "https://webapp-5eb06.firebaseio.com/",
  "storageBucket": "webapp-5eb06.appspot.com"
}

firebase = pyrebase.initialize_app(config)
# print(firebase)

# Get a reference to the database service
db = firebase.database()



def sendDataToFirebase(dataJsonObject):

    print(dataJsonObject)
    db.child("devices").child("dIVh7Zed2jw:APA91bGSPc2NSSjlrscqZLqJKgPa3bf3udtRYerbO9zPzd0Tb8lTcZ5iGVJsboXrXMMAaU8hNUIRsOWBQBBqkeX3V_INk2lDqs2DEAGewQwpoGnaOufBtnhZsOIdizXrDOPNd0mEXLXI").set(dataJsonObject)
    return True

def getDataFromFirebase():
    getDataFromFirebase=dict(db.child("devices").get().val())

    return  getDataFromFirebase

def getGeohashesWithinArea(latitude,longitude, precision,radius):
    candidate_geohashes = ppyh.get_geohash_radius_approximation(latitude,
                                                                longitude,
                                                                radius=radius,
                                                                precision=precision,
                                                                georaptor_flag=False)

    return candidate_geohashes




def getDistance(lat_1, lng_1, lat_2, lng_2):
    R = 6373.0
    lat1 = math.radians(lat_1)
    lon1 = math.radians( lng_1)
    lat2 = math.radians(lat_2)
    lon2 = math.radians(lng_2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c

    return distance


def sendNotification(id,distance,deviceName):

    headers = {
        'Authorization': 'key=AIzaSyCXaaAYR9Es0LCl37-4HwGj3dgVXgMTllg',
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/json',
        'Postman-Token': '727bd893-3986-416d-a376-16ecb6e4e433',
    }

    data1 = '{\n "to" : "fM8V0KvwX9k:APA91bEDcUR0BpJldZ1U5T_g4n6Y1DTZseczBDmE8CcGT3GZoi_qIAF3zbKXXBp3E7xVqh2JAbr_7uLDLRBa_7GE6oCZzl_O9ajomXZn9NoTk12bq_EBQi-yDKrd-gSn5pWrLz6WDRid",\n "collapse_key" : "type_a",\n "notification" : {\n   "title":"Attention ", \n  "body" : "Hazard  Ahead"\n },\n "data" : {\n     "typeOFhazard" : "Accident",\n     "distance": 2,\n     "Severity" : "High",\n     "precaution" : "Go Slow"\n }\n}'
    x = json.loads(data1)
    x["to"]=id
    x["data"]["distance"]=distance
    print("Notification Sent to : "+ deviceName)
    jsonD = json.dumps(x)
    response = requests.post('https://fcm.googleapis.com/fcm/send', headers=headers, data=jsonD)
    print(response)
