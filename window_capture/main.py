import cv2 as cv
import numpy as np
import os
import pyautogui

#changes working directory to folder this script is in
os.chdir(os.path.dirname(os.path.abspath(__file__)))


while(True):
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    #converts screenshot to BGR from RGB
    screenshot = cv.cvtColor(screenshot, cv.Color_RGB2BGR)

    cv.imshow('Computer Vision', screenshot)

    if cv.waitKey(1) == ord('k'):
        cv.destroyAllWindows()
        break
print('Done.')