# -*- coding:utf-8- *-
import numpy as np
import cv2
img = np.zeros((512,512,3), np.uint8)
cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 5)
cv2.circle(img, (447, 63), 50, (0, 0, 255),-1)
cv2.ellipse(img, (256, 256), (100, 50), 90, 0,360, (0, 255, 0), -1)                              
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10], [50, 30], [70, 70]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], False,(255, 255, 0),1)
font = cv2.FONT_HERSHEY_TRIPLEX
cv2.putText(img, 'Ni Hao Ma ?' , (10, 200), font, 1, (255, 0, 0), 1,False)  
cv2.imshow('example', img)
cv2.waitKey(0)
cv2.destroyAllWindows()