# import the necessary packages
import picamdevtool.camtool as camtool
from picamera import PiCamera


try:
    camera = PiCamera()
    
    camtool.init_cam(camera)
    
    frame = camtool.processing_frame(camera)
    while True:
        next(frame)
        #print(frame)
        

except KeyboardInterrupt:
    camera.close()
except:
    camera.close()
    print("something wrong")
finally:
    camera.close()
