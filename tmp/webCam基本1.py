# encoding: utf-8
import cv2
cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture("rtsp://admin:DPUEPA@192.168.1.127:554/stream")
# cap = cv2.VideoCapture("d:/video/ooo.avi")

# 開關狀態判斷
if cap.isOpened():
    print('cam is open')
else:
    print('cam not open')
# 視訊相關參數
for i in range(0,18):
    print(cap.get(i))
# 重新設定解析度
print('*'*20)
ret = cap.set(3,320)
ret = cap.set(4,240) 
# 檢查 # 視訊相關參數
for i in range(0,18):
    print(cap.get(i))

# 調整指定視窗大小
# cv2.resizeWindow('VIDEO',100,100)

# 擷取即時串流影像
while True:
    ret,frame = cap.read()
    # 顯示畫面
    cv2.imshow('VIDEO',frame)
    # 位置設定
    cv2.moveWindow('VIDEO',10,10)

    if cv2.waitKey(1) &0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()    