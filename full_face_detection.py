# -*- coding: utf-8 -*-
"""
Created on Tue May 14 10:44:41 2024

@author: nevin
"""

import cv2
import numpy as np




face=cv2.CascadeClassifier("C://Users//nevin//AppData//Roaming//Python//Python311//site-packages//cv2//data//haarcascade_frontalface_default.xml")
eye=cv2.CascadeClassifier("C://Users//nevin//AppData//Roaming//Python//Python311//site-packages//cv2//data//haarcascade_eye.xml")
smile=cv2.CascadeClassifier("C://Users//nevin//AppData//Roaming//Python//Python311//site-packages//cv2//data//haarcascade_smile.xml")

cap=cv2.VideoCapture(0)

while 1:
    r,image=cap.read()
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
 
    faces=face.detectMultiScale(gray,1.1,3)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),3)
        region_of=gray[y:y+h,x:x+w]
        regionofcolor=image[y:y+h,x:x+w]
        
        eyes=eye.detectMultiScale(region_of,1.1,3)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(regionofcolor,(ex,ey),(ex+ew,ey+eh),(0,255,0),3)
            
        smiles=smile.detectMultiScale(regionofcolor,1.8,5)
        for (sx,sy,sw,sh) in smiles:
            cv2.rectangle(regionofcolor,(sx,sy),((sx+sw),(sy+sh)),(255,0,255),3)
            
    cv2.imshow('face smile',image)
    k=cv2.waitKey(30) & 0xff
    if k==27:
        break

cap.release()
cv2.destroyAllWindows()