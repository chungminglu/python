# encoding: utf-8
import cv2
cap = cv2.VideoCapture(0)
if cap.isOpened():
    print('cam is open')
else:
    print('cam not open')

while True:
    ret,frame = cap.read()
    imSize = cv2.resize(frame,(400,300))
    cv2.imshow('VIDEO',imSize)
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()    