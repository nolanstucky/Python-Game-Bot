import numpy as np
import win32gui, win32ui, win32con

class WindowCapture:

    # properties
    w = 0
    h = 0
    hwnd = None

    def __init__(self, window_name):

        self.hwnd = win32gui.FindWindow(None, window_name)

        self.w = 1920
        self.h = 1080

    def get_screenshot(self):

        bmpfilenamename = "out.bmp" #set this

        
        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj=win32ui.CreateDCFromHandle(wDC)
        cDC=dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0,0),(self.w, self.h) , dcObj, (0,0), win32con.SRCCOPY)
        dataBitMap.SaveBitmapFile(cDC, bmpfilenamename)

        # Free Resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())


