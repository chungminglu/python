import cv2
import os
# cap = cv2.VideoCapture("d:\\xxx1.mp4")
cap = cv2.VideoCapture("rtsp://192.168.43.209:554/h264")
# print(cv2.getBuildInformation())
# os.system("pause")
# cascade_path = "d:\XML\haarcascade_profileface.xml"
# cascade_path = "d:\XML\haarcascade_frontalface_alt2.xml"
cascade_path = "d:\XML\haarcascade_frontalface_alt.xml"

while(1):
    print(cap.get(5))
    ret, frame = cap.read()

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cascade = cv2.CascadeClassifier(cascade_path)
    facerect = cascade.detectMultiScale(frame_gray, scaleFactor=1.3, minNeighbors=5, minSize=(10,10))
    for (x,y,w,h) in facerect:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),1)
        font = cv2.FONT_HERSHEY_TRIPLEX
        cv2.putText(frame,"Searching  .....",(10,100),font,1,(255,255,0),1,False)  
    
    # 縮小畫面顯示
    # imSize = cv2.resize(frame_gray, (640, 480))
    imSize = cv2.resize(frame, (640, 480))    
    cv2.imshow('Opencv',imSize)   

    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()