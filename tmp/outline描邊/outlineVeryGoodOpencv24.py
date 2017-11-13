import cv2  
  
img = cv2.imread('D:/20.jpg')  
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  
  
contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  
cv2.drawContours(img,contours,-1,(0,255,255),1)  
  
cv2.imshow("img", img)  
cv2.waitKey(0)
cv2.destroyAllWindows()