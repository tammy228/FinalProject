import time
import picamera
import numpy as np

try:
    with picamera.PiCamera() as camera:
        camera.resolution = (320, 240)
        camera.framerate = 24
        time.sleep(2)
        output = np.empty((240, 320, 3), dtype=np.uint8)
        camera.capture(output, 'rgb')
        camera.close()
except KeboardInterrupt:
    pass
camera.close()