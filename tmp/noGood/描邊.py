import numpy as np
import cv2
  
im = cv2.imread('d:/19.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)

contours, hierarchy,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print("there are " + str(len(contours)) + " contours")
 
cnt = contours[0]
print("there are " + str(len(cnt)) + " points in contours[0]")
hull = cv2.convexHull(cnt,returnPoints = False)
# defects = cv2.convexityDefects(cnt,hull)
# # print "there are " + str(len(defects)) + " defects in contours[0]"
 
# for i in range(defects.shape[0]):
#     s,e,f,d = defects[i,0]
#     start = tuple(cnt[s][0])
#     end = tuple(cnt[e][0])
#     far = tuple(cnt[f][0])
#     cv2.line(im,start,end,[0,255,0],2)
#     cv2.circle(im,far,5,[0,0,255],-1)
 
# cv2.imshow('im', im)
# cv2.waitKey(0)
cv2.destroyAllWindows()