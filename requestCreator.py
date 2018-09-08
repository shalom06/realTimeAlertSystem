#created By -Shalom Mathews

import firebaseUtilityFunctions as ff

import pygeohash as pgh

precision=5
radius=10

data={
    "name": "SHAL_PC ",
    "logX": 50.404467,
    "logY": -104.598459,
    "alertType": 1,
    "direction":"northeast",
    "geoHash":"c8vwe",
    "token":"dQth04k-AXc:APA91bEdzAlSAvoEz1UY1Wa_U0LySUVd-nZHIUBybbgk5cbBAiP3Xm6urUtISqix0yENsJlUNRjL3uTOmSWO9N_KjXthSXmw42cwowxGlgW3kQPykhN978yixnfwTAk65ymnIoqs_62Y",
    "status": 1
  }
if data["status"]==0:
    successFlag=ff.sendDataToFirebase(data)
    if successFlag:
        print("Done")
else:
    jsonData=ff.getDataFromFirebase()
    centerHash = pgh.encode(data["logX"],data["logY"], precision=precision)

    generateHashCodes=ff.getGeohashesWithinArea(data["logX"],data["logY"],precision,radius)
    ctr=0
    devicesToSend=dict()

    for devValue in jsonData.values():
        print(devValue["geoHash"])
        print(generateHashCodes)
        print(centerHash)
        if devValue["geoHash"] in generateHashCodes or  devValue["geoHash"]== centerHash:
            arrayToSend=list()
            arrayToSend.append("Type OF hazard")
            distance=ff.getDistance(devValue["logX"],devValue["logY"],data["logX"],data["logY"])
            arrayToSend.append(distance)
            arrayToSend.append("Low")
            arrayToSend.append("precaution")
            devicesToSend[devValue["token"]]=arrayToSend
            print(devValue["token"])
            ff.sendNotification(devValue["token"],distance,devValue["name"])



