from flask import Flask,Response
from camera import VideoCamera
app = Flask(__name__)
def gen(camera):
    while True:
        data =  camera.get_frame()
        frame = data[0]
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/')
def video_feed():
    return Response(gen(VideoCamera()),mimetype= 'multipart/x-mixed-replace; boundary=frame')
