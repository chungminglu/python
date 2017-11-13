# encoding: utf-8
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture("d:/18.jpg")
# 畫面大小設定
Width =320
Height = 240
_ = cap.set(3,Width)
_ = cap.set(4,Height) 

r1=0;g1=180;b1=127
while(1):
    lower_color=np.array([b1,g1,r1])
    upper_color=np.array([255,255,255])

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
    # cv2.namedWindow("Result", cv2.WINDOW_NORMAL)      
    cv2.imshow('Result', res)

    # 放置位置
    cv2.moveWindow('Capture',10,10)
    cv2.moveWindow('Mask',10,310)
    cv2.moveWindow('Result',10,610)

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
    print(b1,g1,r1)

cap.release()
cv2.destroyAllWindows()