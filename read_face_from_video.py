# -*- coding: utf-8 -*-
"""
Created on Tue May 14 08:43:56 2024

@author: nevin
"""

import cv2
import numpy as np

face_cascade=cv2.CascadeClassifier("C://Users//nevin//AppData//Roaming//Python//Python311//site-packages//cv2//data//haarcascade_frontalface_default.xml")
capture=cv2.VideoCapture('qwe.mp4')

if(capture.isOpened()==False):
    print("error")
    
while(capture.isOpened()):
    ret,img=capture.read()
    if ret==True:
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            
            
        cv2.imshow('frame',img)
        k=cv2.waitKey(1)
        if k==27:
            break
        
capture.release()
cv2.destroyAllWindows()