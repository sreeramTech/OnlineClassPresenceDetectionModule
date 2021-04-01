import cv2
from imutils.video import WebcamVideoStream
class VideoCamera(object):
    def __init__(self):
        self.stream = WebcamVideoStream(src=0).start()
    def __del__(self):
        self.stream.stop()
    def get_frame(self):
        image =  self.stream.read()
        detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        font = cv2.FONT_HERSHEY_SIMPLEX
        face = detector.detectMultiScale(image,1.1,7)
        for (x,y,h,w) in face:
            cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(image,'Status:Online',(10,450),font,1,(0,255,0),2,cv2.LINE_AA)
        if(len(face) == 0):
            cv2.putText(image,'Status:Offline',(10,450),font,1,(0,0,255),2,cv2.LINE_AA)    
        ret,jpeg = cv2.imencode('.jpg',image)
        data = []
        data.append(jpeg.tobytes())
        return data
