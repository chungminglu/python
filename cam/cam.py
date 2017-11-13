import cv2
vcap = cv2.VideoCapture("rtsp://admin:DPUEPA@192.168.1.127:554/out.h264")
while(True):
    ret, frame = vcap.read()
    cv2.imshow('VIDEO', frame)
    
    key = cv2.waitKey(1) & 0xff
    if key == 27:
        break    