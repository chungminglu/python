import cv2
from threading import Thread

# 多线程，高效读视频
class WebcamVideoStream:
    def __init__(self, src, width, height):
        # initialize the video camera stream and read the first frame
        # from the stream
        self.stream = cv2.VideoCapture(src)
        self.stream.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.stream.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        (self.grabbed, self.frame) = self.stream.read()

        # initialize the variable used to indicate if the thread should
        # be stopped
        self.stopped = False

    def start(self):
        # start the thread to read frames from the video stream
        Thread(target=self.update, args=()).start()
        return self

    def update(self):
        # keep looping infinitely until the thread is stopped
        while True:
            # if the thread indicator variable is set, stop the thread
            if self.stopped:
                return

            # otherwise, read the next frame from the stream
            (self.grabbed, self.frame) = self.stream.read()

    def read(self):
        # return the frame most recently read
        return self.frame

    def stop(self):
        # indicate that the thread should be stopped
        self.stopped = True

# 使用方法
cap = WebcamVideoStream(src="d:/xxx.mp4",width=640,height=480).start()

cascade_path = "d:\XML\cuda\haarcascade_frontalface_alt2.xml"                         
while True:
    frame = cap.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cascade = cv2.CascadeClassifier(cascade_path)
    facerect = cascade.detectMultiScale(frame_gray, scaleFactor=1.3, minNeighbors=5, minSize=(10,10))
    for (x,y,w,h) in facerect:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,127),5)
        font = cv2.FONT_HERSHEY_TRIPLEX
        cv2.putText(frame,"Searching  .....",(10,100),font,1,(255,255,0),1,False)  

    imSize = cv2.resize(frame, (800, 640))    

    cv2.imshow('Opencv',imSize)
    k = cv2.waitKey(500)
    if k == 27:
        break

cap.stop()
cv2.destroyAllWindows()