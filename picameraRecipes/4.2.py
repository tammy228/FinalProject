import time
import picamera
import numpy as np
import cv2

try:
    with picamera.PiCamera() as camera:
        camera.resolution = (320, 240)
        camera.framerate = 24
        time.sleep(2)
        image_np = np.empty((240 * 320 * 3,), dtype=np.uint8)
        camera.capture(image_np, 'bgr')
        image_np = image_np.reshape((240, 320, 3))
        #image_jpg = cv2.imencode(".jpg", image_np)
        image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
        #gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        #cv2.imwrite("arrayObjecttest.jpg", image_jpg)
        cv2.imshow("imdecode", image)
        cv2.waitKey()
        camera.close()
except KeyboardInterrupt:
    pass
    cv2.destroyAllWindows()
    camera.close()
except:
    camera.close()