# -*- coding:utf-8 -*-
from __future__ import print_function
import cv2
import dlib
from boss_train import Model
from whois import who

if __name__ == '__main__':
    # dlib 特徵選取器
    detector = dlib.get_frontal_face_detector()
    cap = cv2.VideoCapture(0)
    # cap = cv2.VideoCapture("rtsp://admin:DPUEPA@192.168.1.127/h264.out")
    # cap = cv2.VideoCapture("d:/video/ooo.avi")
    # cap = cv2.VideoCapture("d:/video/www.mp4")

    # 訓練集載入
    model = Model()
    model.load()
    
    while True:
        ret,frame = cap.read()
        if ret == True:
            color = (0,255,255)
            # 灰階
            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # 使用detector進行人臉辨識
            dets = detector(frame_gray, 1)

            for _, d in enumerate(dets):
                x1 = d.top() if d.top() > 0 else 0
                y1 = d.bottom() if d.bottom() > 0 else 0
                x2 = d.left() if d.left() > 0 else 0
                y2 = d.right() if d.right() > 0 else 0

                # 截圖辨識用 上下,左右
                face = frame[x1:y1,x2:y2]
                
                # # 繪製辨識框 右下,左上
                cv2.rectangle(frame,(y2,y1), (x2,x1) , color, 1)

                # 判斷是誰
                result = model.predict(face)

                # # 判斷後的對應
                who.iswho(result)
                if result == 1 :
                    cv2.rectangle(frame,(y2,y1), (x2,x1) , (255,0,0), 2)
                    font = cv2.FONT_HERSHEY_TRIPLEX
                    cv2.putText(frame,'Hsiung',(x2,x1),font,1,(255,0,0),1,False) 
                elif result == 2 :
                    cv2.rectangle(frame,(y2,y1), (x2,x1) , (0,255,0), 2)
                    font = cv2.FONT_HERSHEY_TRIPLEX
                    cv2.putText(frame,'Math',(x2,x1),font,1,(0,255,0),1,False)                  
                elif result == 3 :
                    cv2.rectangle(frame,(y2,y1), (x2,x1) , (0,0,255), 2)
                    font = cv2.FONT_HERSHEY_TRIPLEX
                    cv2.putText(frame,'Tibame',(x2,x1),font,1,(0,0,255),1,False)  
                else :
                    cv2.rectangle(frame,(y2,y1), (x2,x1) , color, 2)
                    font = cv2.FONT_HERSHEY_TRIPLEX
                    cv2.putText(frame,'else',(x2,x1),font,1,(0,0,0),1,False)     
        else:
            break
        
        # Monitor Video
        imSize = cv2.resize(frame, (1024, 768)) 
        # cv2.namedWindow("Opencv", cv2.WINDOW_NORMAL)
        cv2.imshow('Opencv',imSize)

        if cv2.waitKey(1) == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
