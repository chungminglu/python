# encoding: utf-8
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
# 畫面大小設定,Default is 640x480
#_ = cap.set(3,320)
#_ = cap.set(4,240) 

b1=30;g1=255;r1=255

while(1):
    lower_color=np.array([b1,g1,r1])
    upper_color=np.array([30,255,255])
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    _, binary_B = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(binary_B,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  
    cv2.drawContours(frame,contours,-1,(0,255,255),2)  

    # change to hsv model
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # get mask 2.
    mask = cv2.inRange(hsv, lower_color, upper_color)    
    # detect some color 3.
    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('Result', res)    
    
    # 按鍵控制
    if cv2.waitKey(1) & 0xFF == 27:        
        break
    elif cv2.waitKey(1) & 0xFF == ord('r'):
        r1=r1+1 if r1 < 255 else 255
    elif cv2.waitKey(1) & 0xFF == ord('g'):
        g1=g1+1 if g1 < 255 else 255
    elif cv2.waitKey(1) & 0xFF == ord('b'):
        b1=b1+1 if b1 < 255 else 255

    elif cv2.waitKey(1) & 0xFF == ord('q'):
        r1=r1-1 if r1 > 1 else 0
    elif cv2.waitKey(1) & 0xFF == ord('a'):
        g1=g1-1 if g1 > 1 else 0
    elif cv2.waitKey(1) & 0xFF == ord('z'):
        b1=b1-1 if b1 > 1 else 0
#    print(b1,g1,r1)

cap.release()
cv2.destroyAllWindows()