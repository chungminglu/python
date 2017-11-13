# -*- coding: utf-8 -*-
import cv2
from skimage.filters import threshold_adaptive
from skimage import measure
import numpy as np

cap = cv2.VideoCapture("rtsp://admin:DPUEPA@192.168.1.127:554/out.h264")
cap1 = cv2.VideoCapture("rtsp://admin:ICQWHG@192.168.1.134:554/out.h264")
while(True):
    imgSize = 2.5
    ret,img = cap1.read()
    plate = cv2.medianBlur(img,5) #1~15 模糊度,數字越大越重

    img = cv2.resize(img, (int(1080/imgSize), int(720/imgSize)))
    plate = cv2.resize(plate, (int(1080/imgSize), int(720/imgSize)))

    V = cv2.split(cv2.cvtColor(plate,cv2.COLOR_BGR2HSV))[2]
    thresh = threshold_adaptive(V, 47, offset=15).astype("uint8") * 255
    thresh = cv2.bitwise_not(thresh)    

    cv2.imshow('img',img)
    cv2.imshow('plate',plate)
    cv2.imshow('thresh',thresh)   
         
    if cv2.waitKey(1) == 27:
#    if cv2.waitKey(1) & 0xFF == ord('q'):        
        break
cap.release()
cv2.destroyAllWindows()
