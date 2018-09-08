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



<img src="https://user-images.githubusercontent.com/10242289/45257948-ffd7b780-b36b-11e8-98ac-c39fc7c88dde.png" width="15%"></img> 





Screenshorts in Action






<img src="https://user-images.githubusercontent.com/10242289/45257844-fa796d80-b369-11e8-8aff-ba0f60ed1ee8.png" width="15%"></img> <img src="https://user-images.githubusercontent.com/10242289/45257826-b7b79580-b369-11e8-859a-f8f22bccae24.png" width="15%"></img> 




RealTime Tracking can be seen at https://shalom06.github.io/


<img src="https://user-images.githubusercontent.com/10242289/45258121-a2de0080-b36f-11e8-8aed-19d93b299cd3.png" width="15%"></img> 
