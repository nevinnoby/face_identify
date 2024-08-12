# -*- coding: utf-8 -*-
"""
Created on Mon May 13 21:11:11 2024

@author: nevin
"""

import cv2

face=cv2.CascadeClassifier("C://Users//nevin//AppData//Roaming//Python//Python311//site-packages//cv2//data//haarcascade_frontalface_default.xml")
image=cv2.imread("th.jpeg")
gray=cv2.cvtColor(image,cv2.IMREAD_GRAYSCALE)
faces=face.detectMultiScale(gray,1.1,6)

for(x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),1)
    

print("Faces found",len(faces))
cv2.imshow("faces in the image ",image)
cv2.waitKey()