# encoding: utf-8
import cv2
# cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture("rtsp://admin:DPUEPA@192.168.1.127/stream")
# cap = cv2.VideoCapture("rtsp://admin:DPUEPA@192.168.1.127/h265")
# cap = cv2.VideoCapture("rtsp://admin:DPUEPA@192.168.1.127/h264.out")
cap = cv2.VideoCapture("rtsp://admin:DPUEPA@192.168.1.127/main")
cap1 = cv2.VideoCapture("rtsp://admin:DPUEPA@192.168.1.127/h264.out")

if cap.isOpened():
    print('cam is open')
else:
    print('cam not open')

while True:
    _,frame = cap.read()
    _,frame1 = cap1.read()

    frame = cv2.resize(frame,(400,320))
    frame1 = cv2.resize(frame1,(400,320))    

    cv2.imshow('VIDEO',frame)
    cv2.imshow('VIDEO1',frame1)
    cv2.moveWindow('VIDEO',1200,10)
    cv2.moveWindow('VIDEO1',1200,410)

    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()    