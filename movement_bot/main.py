import pyautogui 
import keyboard
import PIL.ImageGrab
import time

DELAY_BETWEEN_COMMANDS = 0

def main():

    pyAutoGuiFailSafe()
    countDownTimer()

    startEncounters()

    # holdKey('w')
    # holdKey('s')

    print(pyautogui.position())
    print(PIL.ImageGrab.grab().load()[1178,51])
    # print(PIL.ImageGrab.grab().load()[659,942])

def countDownTimer():
    # Countdown timer
    print("Starting", end="")
    for i in range(0, 5):
        print(".", end="", flush=True)
        time.sleep(1)
    print("Go")

def holdKey(key, seconds=0.5):
    pyautogui.keyDown(key)
    time.sleep(seconds)
    pyautogui.keyUp(key)
    time.sleep(DELAY_BETWEEN_COMMANDS)

def pyAutoGuiFailSafe():
    pyautogui.FAILSAFE = True

def startEncounters():
    numberOfEncounters = 0
    while numberOfEncounters < 1:

        pixelEncounterTracker = PIL.ImageGrab.grab().load()[659,942]
        pixelNonEncounterTracker = PIL.ImageGrab.grab().load()[1178,51]

        if keyboard.is_pressed('k'):
            break

        if pixelEncounterTracker == (30,30,30):
            pyautogui.press('8')
            time.sleep(0.5)
            pyautogui.press('8')

        if pixelNonEncounterTracker == (60,232,234):
            holdKey('w')
            holdKey('s')

        print(encounterTracker)
        print(numberOfEncounters)
        time.sleep(1)
        

def encounterTracker():
    pixelEncounterTracker = PIL.ImageGrab.grab().load()[659,942]

    if pixelEncounterTracker == (30,30,30):
        return True
    else:
        return False

if __name__ == "__main__":
    main()