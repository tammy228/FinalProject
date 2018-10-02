from time import sleep
from picamera import PiCamera

try:
    camera = PiCamera()
    camera.start_preview()
    sleep(2)
    for filename in camera.capture_continuous('img{counter:03d}.jpg'):
        print('Captured %s' % filename)
        sleep(5) # wait
except KeyboardInterrupt:
    pass
    camera.stop_preview()