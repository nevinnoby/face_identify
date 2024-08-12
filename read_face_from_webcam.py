# -*- coding: utf-8 -*-
"""
Created on Tue May 14 08:43:27 2024

@author: nevin
"""

import cv2


face=cv2.CascadeClassifier("C://Users//nevin//AppData//Roaming//Python//Python311//site-packages//cv2//data//haarcascade_frontalface_default.xml")

fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('face_out.avi',fourcc,20.0,(640,480))

cap=cv2.VideoCapture(0)

while 1:
    ret,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    faces=face.detectMultiScale(gray,1.1,5)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        
    out.write(img)
    cv2.imshow('face_web',img)
    
    k = cv2.waitKey(30) & 0xFF

    if k==27:
        break
    
    
cap.release()
out.release()

cv2.destroyAllWindows()