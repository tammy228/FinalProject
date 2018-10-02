import time
import picamera
import numpy as np

try:
    # Create an array representing a 1280x720 image of
    # a cross through the center of the display. The shape of
    # the array must be of the form (height, width, color)
    a = np.zeros((720, 1280, 3), dtype=np.uint8)
    a[360, :, :] = 0xff
    a[:, 640, :] = 0xff

    camera = picamera.PiCamera()
    camera.resolution = (1280, 720)
    camera.framerate = 24
    camera.start_preview()
    # Add the overlay directly into layer 3 with transparency;
    # we can omit the size parameter of add_overlay as the
    # size is the same as the camera's resolution
    try:
        o = camera.add_overlay(np.getbuffer(a), layer=3, alpha=64)
    except:
        b = np.arange(a)
        o = camera.add_overlay(b, layer=3, alpha=64)
        
    try:
        # Wait indefinitely until the user terminates the script
        while True:
            time.sleep(1)
    finally:
        camera.remove_overlay(o)
except KeyboardInterrupt:
    pass
camera.stop_preview()
