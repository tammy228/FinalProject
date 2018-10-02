import time
import picamera

try:
    with picamera.PiCamera() as camera:
        camera.resolution = (100, 100)
        camera.start_preview()
        time.sleep(2)
        camera.capture('image.data', 'rgb')
        camera.close()
except KeyboardInterrupt:
    pass
    camera.close()