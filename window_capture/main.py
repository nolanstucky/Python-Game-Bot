import cv2 as cv
import numpy as np
import os
import pyautogui
from time import time
import win32gui, win32ui, win32con

#changes working directory to folder this script is in
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def window_capture():
    # define your monitor width and height
    w = 1920 # set this
    h = 1080 # set this
    bmpfilenamename = "out.bmp" #set this

    hwnd = None
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj=win32ui.CreateDCFromHandle(wDC)
    cDC=dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0,0),(w, h) , dcObj, (0,0), win32con.SRCCOPY)
    dataBitMap.SaveBitmapFile(cDC, bmpfilenamename)

    # Free Resources
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())


loop_time = time()
while(True):


    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)

    #converts screenshot to BGR from RGB

    screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)

    cv.imshow('Computer Vision', screenshot)

    print('FPS {}' .format(1 / (time() - loop_time)))
    loop_time = time()


    if cv.waitKey(1) == ord('k'):
        cv.destroyAllWindows()
        break
print('Done.')