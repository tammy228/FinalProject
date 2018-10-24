import time
import picamera
import os, os.path



try:
    frames = 10
    dir_name = 'picture'
    data_path = '/home/pi/FinalProject/picture'

    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.framerate = 30
        camera.start_preview()
        # Give the camera some warm-up time
        time.sleep(2)
        start = time.time()
		
        camera.capture_sequence([
            './picture/image%02d.jpg' % i
            for i in range(frames)
            ], use_video_port=True)
        finish = time.time()
    print('Captured %d frames at %.2ffps' % (
        frames,
        frames / (finish - start)))
    camera.close()
except KeyboardInterrupt:
    pass
    camera.close()
except:
    camera.close()
