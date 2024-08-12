# -*- coding: utf-8 -*-
"""
Created on Tue May 14 08:15:25 2024

@author: nevin
"""

import urllib.request
import cv2
import numpy as np

face_cascade=cv2.CascadeClassifier("C://Users//nevin//AppData//Roaming//Python//Python311//site-packages//cv2//data//haarcascade_frontalface_default.xml")
url="https://upload.wikimedia.org/wikipedia/commons/a/a5/Tom_cruise_1989.jpg"
url_response=urllib.request.urlopen(url)
image_array=np.array(bytearray(url_response.read()),dtype=np.uint8)
img=cv2.imdecode(image_array,1)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray,1.1,4)

for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    
cv2.imshow("url_image",img)
cv2.waitKey()