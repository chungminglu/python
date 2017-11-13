# encoding: utf-8
import cv2
import numpy as np

# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture("d:/19.jpg")

lower_color=np.array([0,0,0])
upper_color=np.array([0,255,0])

# get a frame and show 1.
ret, frame = cap.read()
cv2.imshow('Capture', frame)

# change to hsv model
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# get mask 2.
mask = cv2.inRange(hsv, lower_color, upper_color)    
cv2.imshow('Mask', frame)

# detect some color 3.
res = cv2.bitwise_and(frame, frame, mask=mask)
# 寻找轮廓
contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# 画出轮廓，-1,表示所有轮廓，画笔颜色为(0, 255, 0)，即Green，粗细为1
cv2.drawContours(res, contours, -1, (0, 255, 255), 1)  
# 显示图片
cv2.namedWindow("Result", cv2.WINDOW_NORMAL)      
cv2.imshow('Result', res)

cv2.waitKey(0) & 0xFF == 27     
cap.release()
cv2.destroyAllWindows()