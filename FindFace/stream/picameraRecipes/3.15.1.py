import picamera
import time

try:
    camera = picamera.PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 24
    camera.start_preview()
    camera.annotate_text = 'Hello world!'
    time.sleep(2)
    # Take a picture including the annotation
    camera.capture('foo.jpg')
    camera.close()
except KeyboardInterrupt:
    pass

camera.close()