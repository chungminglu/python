import cv2
import datetime

face_cascade = cv2.CascadeClassifier('d:/code/xml/haarcascade_frontalface_alt.xml')
# face_cascade = cv2.CascadeClassifier('haarcascade_profileface.xml')
# eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture("/root/Desktop/xxx.mp4")
cap = cv2.VideoCapture("rtsp://admin:DPUEPA@192.168.1.127:554/out.h264")

while(True):
    ret,img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 1)

    for (x,y,w,h) in faces:
    	   cv2.rectangle(img,(x,y),(x+w,y+h),(0,250,0),1)
    	   xx = img[y:y+h, x:x+w]
    	   now = datetime.datetime.now()
    	   cv2.imwrite("d:/code/img/"+ str(now) +".jpg",xx)
    
    imSize = cv2.resize(img, (640, 400)) 
    cv2.imshow('rec',imSize)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
