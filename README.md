# realTimeAlertSystem
Real time alert system using Firebase and Rasberry Pi

1.If no Hazard is detected the data is just stored in Firebase.
2.If Hazard is detected, Data is fetched from firebase and devices which are within a specified radius are calculated using geo-hashing Query and send notifications

Specifications:
Language: Python 3.x
Database: Firebase Real-time Database
Firebase: Firebase is a real time No SQL database System Designed for Fast processing.
IDE : PyCharm
No of Files: 2 
                                

requestCreator.py 
This file is the main driver file which contains the logic.

firebaseUtilityFunctions.py
contains all the utility functions required for reading, Storing, Geo-hashing, FCM Notification System

Flow of code






Screenshorts in Action
