import os
import sys
import numpy
import cv2
import time
import imutils
import shutil

def findface_openCV_forTakingPic(dir_name,pic_abs_path, pic_name):
    start_time = time.time()
    
    haarcascadeVersion = "alt"

    haarcascadeFile = "haarcascade_frontalface_" + haarcascadeVersion +".xml"
    face_cascade = cv2.CascadeClassifier("haarcascades/"+haarcascadeFile)

    processed_face_num = 0
    img = cv2.imread(pic_abs_path)
    print("frame")
    print(img)
    if img is not None:	
	img = imutils.resize(img, width=1280)
        #gray_img = img
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	cnt = 1
	
	face_rects = face_cascade.detectMultiScale(gray_img, 1.3, 5)
        #print(face_rects)
	
        find = 0

	if len(face_rects) == 0 :
            print("alt can't find face , using alt2")
            haarcascadeVersion = "alt2"
            haarcascadeFile = "haarcascade_frontalface_" + haarcascadeVersion +".xml"
            face_cascade = cv2.CascadeClassifier("haarcascades/"+haarcascadeFile)
            face_rects2 = face_cascade.detectMultiScale(gray_img, 1.3, 5)
            if len(face_rects2) == 0:
                print("alt2 can't find face , using alt_tree")
                haarcascadeVersion = "alt_tree"
                haarcascadeFile = "haarcascade_frontalface_" + haarcascadeVersion +".xml"
                face_cascade = cv2.CascadeClassifier("haarcascades/"+haarcascadeFile)
                face_rects3 = face_cascade.detectMultiScale(gray_img, 1.3, 5)
                if len(face_rects3) == 0:
                    print("alt_tree can't find face , using default")
                    haarcascadeVersion = "default"
                    haarcascadeFile = "haarcascade_frontalface_" + haarcascadeVersion +".xml"
                    face_cascade = cv2.CascadeClassifier("haarcascades/"+haarcascadeFile)
                    face_rects4 = face_cascade.detectMultiScale(gray_img, 1.3, 5)
                    face_rects0 = face_rects4
                    print("use default")
                else:
                    face_rects0 = face_rects3
                    print("use alt_tree")
            else:
                face_rects0 = face_rects2
                print("use alt2")
        else:
            face_rects0 = face_rects
            print("use alt")

        #print(face_rects0)

        for(x, y, w, h) in face_rects0:
	    x1 = x
            y1 = y
            x2 = x + w
            y2 = y + h

            imgShot = gray_img[y1:y2, x1:x2]
            #cv2.imwrite(["./%s/num_{counter:03d}%s" % (dir_name,pic_name)  ], imgShot)
            imgShotpath =  str(cnt) +"_"+ pic_name
            cv2.imwrite("./" + dir_name+ "/"+ imgShotpath, imgShot)
            #cv2.imshow("i", imgShot)
            #cv2.waitKey(0)
            #print(pic_abs_path)
	    cnt+=1
	    processed_face_num += 1
            shutil.move("/home/pi/FinalProject/media/" + imgShotpath,"/home/pi/FinalProject/second_picture")

			
    print("{} takes --- {} seconds to --- find {} faces".format( sys.argv[0], (time.time() - start_time), processed_face_num) )



def findface_dlib_forTraining():
    start_time = time.time()

    if (len(sys.argv) < 2):
            print("Forgot directory name argument. Please try again.")
            sys.exit()

    haarcascadeVersion = sys.argv[2]
    #haarcascadeVersion = "default"
    #haarcascadeVersion = "alt"
    #haarcascadeVersion = "alt2"
    #haarcascadeVersion = "alt_tree"

    haarcascadeFile = "haarcascade_frontalface_" + haarcascadeVersion +".xml"

    top = sys.argv[1]
    OUTPUT = "OUTPUT/"
    OUTPUT_DIR = OUTPUT+"Output_openCV_" + haarcascadeVersion + "_"  + sys.argv[1]

    if not os.path.exists(OUTPUT):
            os.mkdir(OUTPUT)

    # get a trained face data to detect face
    if not os.path.exists("haarcascades/"+haarcascadeFile):
            print("Could not find haarcascade file. Please put it in the same directory with this python file")
    face_cascade = cv2.CascadeClassifier("haarcascades/"+haarcascadeFile)

    #
    #face_coord_txt_index = filenames.index('bounding_boxes_37300.txt')
    #face_coordinate_file = filenames.pop(face_coord_txt_index)

    if not os.path.exists(OUTPUT_DIR):
            os.mkdir(OUTPUT_DIR)

    processed_face_num = 0

    for rootdir, dirs, files in os.walk(top, topdown=False):
            for dirname in dirs:
                    print("    "+dirname+"====================")

                    # create sub directory in output directory
                    OUTPUT_subdir = os.path.join(OUTPUT_DIR, dirname)
                    if not os.path.exists(OUTPUT_subdir):
                            os.mkdir(OUTPUT_subdir)

                    # get every sub directory's absolute route according to operating systems
                    abs_dirname = os.path.join(rootdir, dirname)
                    files = os.listdir(abs_dirname)

                    for filename in files:
                            print("       start processing " + filename + "...")

                            # get every file's absolute route according to operating systems
                            abs_filename = os.path.join(abs_dirname, filename)

                            img = cv2.imread(abs_filename)

                            # because .gif can't be read by cv2.imread, so we need a expression to be a filter.
                            if img is not None:
                                    # Turns img from BGR (color sheme) int gray
                                    print("        img color to gray")
                                    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                                    # search cascade classifiet ?
                                    face_rects = face_cascade.detectMultiScale(gray_img, 1.3, 5)
                                    
                                    # to draw rectangles on every face in image
                                    cnt = 1
                                    for(x, y, w, h) in face_rects:
                                            # to draw rectangles on a face
                                            x1 = x
                                            y1 = y
                                            x2 = x + w
                                            y2 = y + h
                                            cv2.rectangle(img, (x1,y1), (x2, y2), (255, 0, 0), 2)
                                            grayShot = gray_img[y1:y2, x1:x2]

                                            # to draw the face's eyes with rectangles
                                            '''
                                            roi_color = img[y1:y2, x1:x2]
                                            eyes = eye_cascade.detectMultiScale(roi_gray)
                                            for(ex,ey,ew,eh) in eyes:
                                                    cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0, 255, 0), 2)
                                            '''

                                            # store cutting face for preprocess image into output directory
                                            cv2.imwrite(OUTPUT_DIR+"/"+dirname+"/"+str(cnt)+"_"+filename, grayShot)
                                            print("Image Shot "+dirname+" "+str(cnt)+"_"+filename+" has been processed")
                                            cnt+=1
                                            processed_face_num+=1

                            print("Images "+ filename +" has been processed")	
                    print("Images in dir " + dirname + " has been processed")

    '''
            #for image in filenames:
            video_capture = cv2.VideoCapture(image)

        # Reads the image out of the file
            return_value, cv_frame = video_capture.read()
    '''	

    print("All images have been processed!!!")
    print("--- {} seconds --- find {} faces".format( (time.time() - start_time), processed_face_num) )
    cv2.waitKey(0)
    cv2.destroyAllWindows()
