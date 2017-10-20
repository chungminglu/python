import numpy as np
import cv2
import datetime

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
# face_cascade = cv2.CascadeClassifier('haarcascade_profileface.xml')
# eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture("/root/Desktop/xxx.mp4")

while(True):
    _,img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 2)

    for (x,y,w,h) in faces:
    	   cv2.rectangle(img,(x,y),(x+w,y+h),(0,250,0),5)
    	   # print("x,y,w,h",x,y,w,h)

    	   xx = img[y:y+h, x:x+w]
    	   now = datetime.datetime.now()
    	   cv2.imwrite("./img/"+ str(now) +".jpg",xx)
	
    	   # roi_gray = gray[y:y+h, x:x+w]
    	   # roi_color = img[y:y+h, x:x+w]

    	   # eyes = eye_cascade.detectMultiScale(roi_gray)
    	   # for (ex,ey,ew,eh) in eyes:
    	   #     cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    
    cv2.imshow('rec',img)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
    elif cv2.waitKey(10) & 0xFF == ord("s"):
    	now = datetime.datetime.now()
		# ts = now.strftime("%Y-%m-%d %H:%M:%S")	
    	cv2.imwrite("./img"+ str(now) +".jpg",xx)

cap.release()
cv2.destroyAllWindows()
