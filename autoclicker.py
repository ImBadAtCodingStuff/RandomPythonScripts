
# move mouse side to side

import pyautogui
from time import sleep


def move_right():
    # move right
    pyautogui.moveRel(100, 0)


def move_left():
    # move left
    pyautogui.moveRel(-100, 0)


while 1:
    move_left()
    sleep(.1)
    move_right()
    sleep(.1)
