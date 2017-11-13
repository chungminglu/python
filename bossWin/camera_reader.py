# -*- coding:utf-8 -*-
import os
import cv2
#import subprocess
#import serial
import time
from boss_train import Model
#from image_show import show_image

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    # cap = cv2.VideoCapture('d:/video/1.mp4')    
    #cap = cv2.VideoCapture('rtsp://192.168.43.209:554')
    cascade_path = "d:/code/python/bossWin/haarcascade_frontalface_alt.xml"
    model = Model()
    model.load()
    
    while True:
        _, frame = cap.read()
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cascade = cv2.CascadeClassifier(cascade_path)

        # facerect = cascade.detectMultiScale(frame_gray,1.03,1)
        facerect = cascade.detectMultiScale(frame_gray, scaleFactor=1.4, minNeighbors=10, minSize=(10,10))
        # facerect = cascade.detectMultiScale(frame_gray, scaleFactor=1.01, minNeighbors=3, minSize=(3, 3))

        for (x,y,w,h) in facerect:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(127,255,0),1)
            font = cv2.FONT_HERSHEY_TRIPLEX
            cv2.putText(frame,"Searching  .....",(10,100),font,1,(255,255,0),1,False)             
        # cv2.imshow('Opencv',frame)

        if len(facerect) > 0:
            # print('face detected')
            color = (255, 255, 255)  # 白
            for rect in facerect:
                #cv2.rectangle(frame, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]), color, thickness=2)

                # 0&1 is Start position,2&3 is width&height
                x, y = rect[0:2]
                width, height = rect[2:4]
                
                # cut the image area from opencv to keras
                # image = frame[y - 10: y + height, x: x + width]
                image = frame[y - 50: y + height, x - 50: x + width]
                # print(x,y,height,width)
                # print(type(image))
                
                # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                # cv2.imshow('Opencv',gray)
           
                result = model.predict(image)
                # print(result)
                if result == 0:  # boss
                    # print('Boss is approaching')
                    # show_image()
                    # print("xxx-xxx-xxx")

                    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                    # print(gray)
                    if gray is not None:
                        # cv2.imshow('Opencv',gray) 

                        font = cv2.FONT_HERSHEY_TRIPLEX
                        cv2.putText(frame,"SeaFood !! .....",(10,300),font,3,(0,0,255),1,False) 


                        # os.system('spd-say "sea food"')
                        # time.sleep(1)
                        # ser = serial.Serial(
                        #     port='/dev/ttyUSB0',
                        #     baudrate=9600,
                        #     parity=serial.PARITY_NONE,
                        #     stopbits=serial.STOPBITS_ONE,
                        #     bytesize=serial.EIGHTBITS,
                        #     xonxoff=serial.XOFF,
                        #     rtscts=False,
                        #     dsrdtr=False
                        # )
                        # # ser.open()
                        # # ser.isOpen()
                        # print("Initializing the device ..")
                        # ser.write('Not Boss !! \n'.encode())
                        # print("Write command")
                        # # ser.write (bytes(0x04))
                        # print('Done')                                                           
                # else:
                #     print('Not boss')
                    # os.system('spd-say "Who are you"')
        imSize = cv2.resize(frame, (800, 600)) 

        cv2.imshow('Opencv',imSize)

        k = cv2.waitKey(1)
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
