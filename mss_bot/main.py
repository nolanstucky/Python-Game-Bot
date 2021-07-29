import cv2 as cv
import numpy as np
import os
from time import time
from mss import mss
import imutils

# from vision import Vision

#changes working directory to folder this script is in
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# luma_star = Vision('luma_star.jpg')

template = cv.imread("grass.jpg")
template = cv.cvtColor(template, cv.COLOR_BGR2GRAY)
template = cv.Canny(template, 50, 200)
(h, w) = template.shape[:2]

with mss() as sct:
    # Part of the screen to capture
    monitor = {"top": 40, "left": 0, "width": 1280, "height": 1000}
    

    while "Screen capturing":
        last_time = time()

        # Get raw pixels from the screen, save it to a Numpy array
        img = np.array(sct.grab(monitor))
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        edged = cv.Canny(gray, 50, 200)

        found = None

        for scale in np.linspace(0.2, 1.0, 20)[::-1]:
            resized = imutils.resize(gray, width=int(gray.shape[1] * scale))
            r = gray.shape[1] / float(resized.shape[1])

            if resized.shape[0] < h or resized.shape[1] < w:
                break

            edged = cv.Canny(resized, 50, 200)
            cv.imwrite("canny_image.png", edged)
            result = cv.matchTemplate(edged, template, cv.TM_CCOEFF)
            (_, maxVal, _, maxLoc) = cv.minMaxLoc(result)

            if found is None or maxVal > found[0]:
                found = (maxVal, maxLoc, r)

        (_, maxLoc, r) = found
        (startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
        (endX, endY) = (int((maxLoc[0] + w) * r), int((maxLoc[1] + h) * r))

        cv.rectangle(img, (startX, startY), (endX, endY), (180, 105, 255), 2)

        # print('The loop took: {0}'.format(time.time()-last_time))
        cv.imshow('test', np.array(img))
        
        print(maxVal)

        # Display the picture
        # screenshot = cv.imshow("Computer Vision", img)

        # Display the picture in grayscale
        # screenshot = cv2.imshow('OpenCV/Numpy grayscale',
        #                 cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))

        # luma_star.find(screenshot, 0.6, 'rectangles')

        

        print("fps: {}".format(1 / (time() - last_time)))

        # Press "q" to quit
        if cv.waitKey(25) & 0xFF == ord("q"):
            cv.destroyAllWindows()
            break
print('Done.')