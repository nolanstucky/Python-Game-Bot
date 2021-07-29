import cv2 as cv
import numpy as np
import os
from time import time
from windowcapture import WindowCapture
from vision import Vision

os.chdir(os.path.dirname(os.path.abspath(__file__)))

wincap = WindowCapture()

luma_star = Vision('run.JPG')

loop_time = time()
while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()

    # display the processed image
    points = luma_star.find(screenshot, 0.5, 'rectangles')
    #points = vision_gunsnbottle.find(screenshot, 0.7, 'points')

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')