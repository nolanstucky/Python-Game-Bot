import cv2 
import numpy 
import os
from time import time
from windowcapture import WindowCapture
from mss import mss

#changes working directory to folder this script is in
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# wincap = WindowCapture('Steam')

# WindowCapture.list_window_names()

# loop_time = time()
# while(True):


#     # screenshot = wincap.get_screenshot()

#     cv.imshow('Computer Vision', screenshot)

#     print('FPS {}' .format(1 / (time() - loop_time)))
#     loop_time = time()


#     if cv.waitKey(1) == ord('k'):
#         cv.destroyAllWindows()
#         break


# print('Done.')

with mss() as sct:
    # Part of the screen to capture
    monitor = {"top": 40, "left": 0, "width": 1280, "height": 1040}

    while "Screen capturing":
        last_time = time()

        # Get raw pixels from the screen, save it to a Numpy array
        img = numpy.array(sct.grab(monitor))

        # Display the picture
        cv2.imshow("OpenCV/Numpy normal", img)

        # Display the picture in grayscale
        # cv2.imshow('OpenCV/Numpy grayscale',
        #            cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))

        print("fps: {}".format(1 / (time() - last_time)))

        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break