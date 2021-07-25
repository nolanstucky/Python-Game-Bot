import pyautogui 
import keyboard
import PIL.ImageGrab
import time

DELAY_BETWEEN_COMMANDS = 0

def main():

    pyAutoGuiFailSafe()
    countDownTimer()

    # startEncounters()



    # holdKey('w')
    # holdKey('s')

    print(pyautogui.position())

    

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
    NUMBER_OF_ENCOUNTERS = 0
    while NUMBER_OF_ENCOUNTERS < 500:
        if keyboard.is_pressed('k'):
            break

        
        print(NUMBER_OF_ENCOUNTERS)
        time.sleep(1)

        NUMBER_OF_ENCOUNTERS += 1

if __name__ == "__main__":
    main()