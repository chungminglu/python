import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as image

I = image.imread('d:/18.jpg') 
G = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)

# Canny Edge Detection:
Threshold1 = 150;
Threshold2 = 350;
FilterSize = 5

E = cv2.Canny(G, Threshold1, Threshold2, FilterSize)
rho = 1
Thetares = 1*np.pi/180
Threshold = 100
minLineLength = 100
maxLineGap = 50

lines = cv2.HoughLinesP(E,rho,Thetares,Threshold,minLineLength,maxLineGap)

# lines = cv2.HoughLinesP(E,rho= 1,theta = 1*np.pi/180,threshold = 100,minLineLength = 100,maxLineGap = 50)

N = lines.shape[0]
print(N)

for i in range(N):
    x1 = lines[i][0][0]
    y1 = lines[i][0][1]    
    x2 = lines[i][0][2]
    y2 = lines[i][0][3]    
    cv2.line(I,(x1,y1),(x2,y2),(255,0,0),1)

plt.figure()
plt.imshow(I)
plt.title('Hough Lines')
plt.axis('off')
plt.show()