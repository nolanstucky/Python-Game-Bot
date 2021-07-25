import pyautogui   
import time

def main():

    pyautogui.FAILSAFE = True

    # Countdown timer
    print("Starting", end="")
    for i in range(0, 5):
        print(".", end="")
        time.sleep(1)
    print("Go")

    pyautogui.keyDown('w')
    time.sleep(0.5)
    pyautogui.keyUp('w')

    pyautogui.keyDown('s')
    time.sleep(0.5)
    pyautogui.keyUp('s')


if __name__ == "__main__":
    main()