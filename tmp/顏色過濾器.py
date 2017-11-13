import cv2
import numpy as np

cap = cv2.VideoCapture(0)

r1=0;g1=255;b1=127
while(1):
    lower_color=np.array([b1,g1,r1])
    upper_color=np.array([255,255,255])

    # get a frame and show
    ret, frame = cap.read()
    cv2.imshow('Capture', frame)

    # change to hsv model
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # get mask
    mask = cv2.inRange(hsv, lower_color, upper_color)
    cv2.imshow('Mask', mask)

    # detect blue
    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('Result', res)

    # 放置位置
    cv2.moveWindow('Capture',10,10)
    cv2.moveWindow('Mask',660,10)
    cv2.moveWindow('Result',1310,10)

    # 按鍵控制
    if cv2.waitKey(1) & 0xFF == 27:        
        break
    elif cv2.waitKey(1) & 0xFF == ord('r'):
        r1=r1+5 if r1 < 250 else 255
    elif cv2.waitKey(1) & 0xFF == ord('g'):
        g1=g1+5 if g1 < 250 else 255
    elif cv2.waitKey(1) & 0xFF == ord('b'):
        b1=b1+5 if b1 < 250 else 255

    elif cv2.waitKey(1) & 0xFF == ord('q'):
        r1=r1-5 if r1 > 5 else 0
    elif cv2.waitKey(1) & 0xFF == ord('a'):
        g1=g1-5 if g1 > 5 else 0
    elif cv2.waitKey(1) & 0xFF == ord('z'):
        b1=b1-5 if b1 > 5 else 0
    print(b1,g1,r1)

cap.release()
cv2.destroyAllWindows()