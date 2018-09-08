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






<img src="https://user-images.githubusercontent.com/10242289/45257844-fa796d80-b369-11e8-8aff-ba0f60ed1ee8.png" width="15%"></img> <img src="https://user-images.githubusercontent.com/10242289/45257826-b7b79580-b369-11e8-859a-f8f22bccae24.png" width="15%"></img> 
