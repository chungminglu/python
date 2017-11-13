#載入必要的packages
from __future__ import print_function
#下方的步驟中, 我們使用skimage提供的Adaptive threshold而非OpenCV
from skimage.filters import threshold_adaptive
#Connected-component labeling相關功能就放在skimage的子模組measure
from skimage import measure
import numpy as np
import cv2
image = cv2.imread("d:/tmp/b2.png")
plate = cv2.medianBlur(image,5)
#將圖片由RGB轉為HSV格式，然後取HSV中的Ｖ值，此效果與灰階效果類似。
V = cv2.split(cv2.cvtColor(plate, cv2.COLOR_BGR2HSV))[2]
#使用skimage提供的Adaptive threshold
thresh = threshold_adaptive(V, 47, offset=15).astype("uint8") * 255
thresh = cv2.bitwise_not(thresh)
#顯示原圖及Threshold處理後的圖片
cv2.imshow("License Plate", plate)
cv2.imshow("Thresh", thresh)
#針對thresholded圖片進行connected components analysis，
# neighbors=8表示採用8向方式, background=0表示pixel值為0則認定為背景
labels = measure.label(thresh, neighbors=8, background=0)
#建立一個空的圖，存放稍後將篩選出的字母及數字
mask = np.zeros(thresh.shape, dtype="uint8")
#顯示一共貼了幾個Lables（即幾個components）
print("[INFO] Total {} blobs".format(len(np.unique(labels))))
#依序處理每個labels
for (i, label) in enumerate(np.unique(labels)):
#如果label==0，表示它為背景
    if label == 0:
        print("[INFO] label: 0 (background)")
        continue
#否則為前景，顯示其label編號i
print("[INFO] label: {} (foreground)".format(i))
#建立該前景的Binary圖
labelMask = np.zeros(thresh.shape, dtype="uint8")
labelMask[labels == label] = 255
#有幾個非0的像素?
numPixels = cv2.countNonZero(labelMask)
#如果像素數目在2500~4000之間認定為車牌字母或數字
if numPixels > 2500 and numPixels < 4000:
#放到剛剛建立的空圖中
    mask = cv2.add(mask, labelMask)
#顯示該前景物件
cv2.imshow("Label", mask)
# cv2.imshow("Label", labelMask)
cv2.waitKey(0)
#顯示所抓取到的車牌