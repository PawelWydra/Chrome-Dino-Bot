import pyautogui
import time
import keyboard


def jump():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    pyautogui.keyUp('space')
    print('Jump')


### Get  coordinates by pyautogui.displayMousePosition() ###

while not keyboard.is_pressed("q"):
    if pyautogui.pixel(480, 425)[0] == 83 or pyautogui.pixel(437, 425)[0] == 83:
        jump()
