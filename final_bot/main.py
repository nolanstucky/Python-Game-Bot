import cv2 as cv
import numpy as np
import os
from time import time
from windowcapture import WindowCapture
from vision import Vision

os.chdir(os.path.dirname(os.path.abspath(__file__)))

wincap = WindowCapture()

# luma_star = Vision('grass.JPG')

cascade_grass = cv.CascadeClassifier('cascade/cascade.xml')

vision_grass = Vision(None)

loop_time = time()
while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()



    # points = luma_star.find(screenshot, 0.35, 'rectangles')

    rectangles = cascade_grass.detectMultiScale(screenshot)

    detection_image = vision_grass.draw_rectangles(screenshot, rectangles)

    cv.imshow('Unprocessed', detection_image)

    print(vision_grass.get_click_points(rectangles))

    # debug the loop rate
    # print('FPS {}'.format(1 / (time() - loop_time)))
    # loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    key = cv.waitKey(1)

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
    elif key == ord('k'):
        cv.imwrite('positive_matches/{}.jpg'.format(loop_time), screenshot)
    elif key == ord('l'):
        cv.imwrite('negative_matches/{}.jpg'.format(loop_time), screenshot)

print('Done.')