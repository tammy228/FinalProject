import time
import picamera

try:
    frames = 10

    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.framerate = 30
        camera.start_preview()
        # Give the camera some warm-up time
        time.sleep(2)
        start = time.time()
		timestamp = time.strftime("%Y%m%d%H%M%S")
        camera.capture_sequence([
            './photo/image%02d.jpg' % i
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
